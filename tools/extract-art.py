"""Lifts the bomb rack out of KSArmory's shared atlas into this mod's own.

    blender --background --python tools/extract-art.py -- <ksarmory.glb> <out.glb>

Run once. Its output is committed, exactly as KSArmory commits its own atlas -- this is here so
the provenance of the mesh is recoverable, not because a pack needs Blender to build.

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

bpy.ops.object.select_all(action="SELECT")
bpy.ops.export_scene.gltf(
    filepath=out, export_format="GLB", export_yup=False,
    use_selection=True, export_apply=True,
    export_cameras=False, export_lights=False)

print(f"wrote {out}: {sorted(ob.name for ob in bpy.data.objects)}")
