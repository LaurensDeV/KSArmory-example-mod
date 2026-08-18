"""Lifts the bomb rack out of KSArmory's shared atlas into this mod's own.

    blender --background --python tools/extract-art.py -- <ksarmory.glb> <out.glb>

Run once. Its output is committed, exactly as KSArmory commits its own atlas -- this is here so
the provenance of the mesh is recoverable, not because a pack needs Blender to build.

The geometry was generated, not modelled: KSArmory built it from primitives in
tools/model/bombrack.py, which was deleted from that repository when the rack moved here. To
change the shape rather than the numbers, either recover that script from KSArmory's history or
model a replacement -- there is no build step in this mod that can regenerate the mesh.

The UVs are left alone and point into the same 4x4 palette, so the textures are copied across
rather than rebaked. That is the whole reason this is a copy and not a re-authoring: the geometry
is a handful of flat-swatch primitives and the colour lives in the UVs.
"""
import sys

import bpy

KEEP = {
    "KSArmory_Subpart_BombRack": "ExampleMod_Subpart_BombRack",
    "KSArmory_Subpart_BombRack_VM": "ExampleMod_Subpart_BombRack_VM",
    "KSArmory_Subpart_Mk82": "ExampleMod_Subpart_Mk82",
    "KSArmory_Subpart_Mk82_VM": "ExampleMod_Subpart_Mk82_VM",
}

source, out = sys.argv[sys.argv.index("--") + 1:]

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=source)

for ob in list(bpy.data.objects):
    if ob.name not in KEEP:
        bpy.data.objects.remove(ob, do_unlink=True)

missing = KEEP.keys() - {ob.name for ob in bpy.data.objects}
if missing:
    raise SystemExit(f"not in the source atlas: {sorted(missing)}")

# Orphans left by the deletions own the names we are about to claim, and Blender answers a
# collision by silently appending .001 -- which exports a node whose mesh has a different name,
# breaking the one rule KSA actually enforces about a .glb.
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

for ob in list(bpy.data.objects):
    ob.name = KEEP[ob.name]
    ob.data.name = ob.name

# export_yup=True, which looks wrong beside KSArmory's own generator and is not.
#
# KSA reads a .glb raw, so the generator *builds* in Blender coordinates and exports with +Y Up
# OFF. This script does not build: it imports, and Blender's glTF importer always converts Y-up to
# Z-up with no option to decline. Exporting with +Y Up OFF then skips the inverse and the geometry
# lands rotated a quarter turn about X -- which for this part swings the bomb's axis off the
# launch tube and onto the hull tangent, so it hangs sideways. A round trip needs both halves.
bpy.ops.object.select_all(action="SELECT")
bpy.ops.export_scene.gltf(
    filepath=out, export_format="GLB", export_yup=True,
    use_selection=True, export_apply=True,
    export_cameras=False, export_lights=False)

print(f"wrote {out}: {sorted(ob.name for ob in bpy.data.objects)}")


def bounds(path):
    """Every object's world-space bounding box, as this importer sees it."""
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=path)

    boxes = {}
    for ob in bpy.data.objects:
        xs = [ob.matrix_world @ v.co for v in ob.data.vertices]
        boxes[ob.name] = tuple(round(max(c[i] for c in xs) - min(c[i] for c in xs), 5) for i in range(3))

    return boxes


# The check that would have caught the axis swap. checkmesh.py cannot: it asks about UV area and
# coplanar faces, and a body rotated a quarter turn is clean by both. Nothing else compares what
# was written against what was read, and the symptom in game is a bomb hanging sideways.
was, now = bounds(source), bounds(out)
for old, new in KEEP.items():
    if was[old] != now[new]:
        raise SystemExit(f"{new} is {now[new]} but {old} was {was[old]} -- the export moved it")

print(f"verified: {len(KEEP)} mesh(es) came through the same size as they went in")
