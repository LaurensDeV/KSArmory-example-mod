# The example copy: every KSArmory weapon as a pack

Generated from KSArmory `c138556f35` (2026-10-22) by `tools/export-example-copy.py` in that repository. Do not edit these files; they are overwritten. What is generated is listed below, and the Mk 82 rack beside it is this mod's own.

Every weapon KSArmory ships, defined the way any pack defines one: the definitions in `KSArmory/`, the parts in `ExampleCopyAssets.xml` and `ExampleCopyGameData.xml`, the gun sounds in `ExampleCopySounds.xml`, and the art in `Meshes/`, `Textures/` and `Sounds/`, all under `ExampleCopy_` Ids so it loads beside KSArmory. The parts are named with `(copy)` in the editor.

**To fly the copy alone**, switch every family off under *KSArmory > Built-in weapons* and restart. KSArmory's own parts then load as structure and leave the editor, and every weapon there is one of these. A craft needs the copy's parts to carry them: KSArmory's `tools/copy-save.py` makes a save's craft carry them instead.

To start your own from one, copy what that family uses below under Ids of your own. A marker a definition names is found inside the Id the `<Part>` gives a subpart, not the template's. A gun naming no sound plays KSArmory's `KSArmoryCannon`, and the plume, flash and smoke are KSArmory's effects for every pack.

## By family

### Countermeasures: [`KSArmory/Countermeasures.xml`](KSArmory/Countermeasures.xml)

`<Decoy>` and `<Dispenser>`: one kind of decoy per part.

- **Parts:** `ExampleCopy_Prefab_Ale47Chaff`, `ExampleCopy_Prefab_Ale47Flare`, in `ExampleCopyAssets.xml` and `ExampleCopyGameData.xml`
- **Meshes:** `Meshes/ExampleCopy_Ale47.glb`
- **Textures:** `Textures/ExampleCopy_Ale47_Diffuse.png`, `Textures/ExampleCopy_Ale47_Normal.png`, `Textures/ExampleCopy_Ale47_PBR.png`
- **Sounds it names:** none of its own
- [KSArmory's own file at that commit](https://github.com/LaurensDeV/KSArmory/blob/c138556f35eba603f9de60320a744852f5b3bd57/src/KSArmory/KSArmory/Countermeasures.xml)

### DirectedEnergy: [`KSArmory/DirectedEnergy.xml`](KSArmory/DirectedEnergy.xml)

A beam weapon: `<Beam>` inside an `<Optic>`, and a `<Launcher>` with `FiresBeam` and no round.

- **Parts:** `ExampleCopy_Prefab_Yal1Turret`, in `ExampleCopyAssets.xml` and `ExampleCopyGameData.xml`
- **Meshes:** `Meshes/ExampleCopy_Yal1.glb`
- **Textures:** `Textures/ExampleCopy_Yal1_Diffuse.png`, `Textures/ExampleCopy_Yal1_Normal.png`, `Textures/ExampleCopy_Yal1_PBR.png`
- **Sounds it names:** none of its own
- [KSArmory's own file at that commit](https://github.com/LaurensDeV/KSArmory/blob/c138556f35eba603f9de60320a744852f5b3bd57/src/KSArmory/KSArmory/DirectedEnergy.xml)

### Guns: [`KSArmory/Guns.xml`](KSArmory/Guns.xml)

Guns with no tubes: `<Muzzle>`, belts and bursts, a rotary cluster, a time-fuzed shell, a chin turret's travel limit, and the cylinder and rod drawn on its linkage.

- **Parts:** `ExampleCopy_Prefab_Ciws`, `ExampleCopy_Prefab_M197`, `ExampleCopy_Prefab_Mk42`, in `ExampleCopyAssets.xml` and `ExampleCopyGameData.xml`
- **Meshes:** `Meshes/ExampleCopy_Ciws.glb`, `Meshes/ExampleCopy_M197.glb`, `Meshes/ExampleCopy_Mk42.glb`
- **Textures:** `Textures/ExampleCopy_Ciws_Diffuse.png`, `Textures/ExampleCopy_Ciws_Normal.png`, `Textures/ExampleCopy_Ciws_PBR.png`, `Textures/ExampleCopy_M197_Diffuse.png`, `Textures/ExampleCopy_M197_Normal.png`, `Textures/ExampleCopy_M197_PBR.png`, `Textures/ExampleCopy_Mk42Shell_Diffuse.png`, `Textures/ExampleCopy_Mk42Shell_Normal.png`, `Textures/ExampleCopy_Mk42Shell_PBR.png`, `Textures/ExampleCopy_Mk42_Diffuse.png`, `Textures/ExampleCopy_Mk42_Normal.png`, `Textures/ExampleCopy_Mk42_PBR.png`
- **Sounds it names:** `Sounds/ExampleCopy_M197_Loop.wav`, `Sounds/ExampleCopy_M197_Tail.wav`, `Sounds/ExampleCopy_Mk42_Gunshot.wav`
- [KSArmory's own file at that commit](https://github.com/LaurensDeV/KSArmory/blob/c138556f35eba603f9de60320a744852f5b3bd57/src/KSArmory/KSArmory/Guns.xml)

### Pantsir: [`KSArmory/Pantsir.xml`](KSArmory/Pantsir.xml)

A launcher that traverses and elevates, twelve tubes in two pods, a cannon on the same traverse, and a director on its roof (`<Optic>` beside a `<Launcher>` on one part).

- **Parts:** `ExampleCopy_Prefab_Launcher6`, in `ExampleCopyAssets.xml` and `ExampleCopyGameData.xml`
- **Meshes:** `Meshes/ExampleCopy_MeshAtlas.glb`
- **Textures:** `Textures/ExampleCopy_Diffuse.png`, `Textures/ExampleCopy_Normal.png`, `Textures/ExampleCopy_PBR.png`
- **Sounds it names:** none of its own
- [KSArmory's own file at that commit](https://github.com/LaurensDeV/KSArmory/blob/c138556f35eba603f9de60320a744852f5b3bd57/src/KSArmory/KSArmory/Pantsir.xml)

### Rails: [`KSArmory/Rails.xml`](KSArmory/Rails.xml)

A launcher with nothing that moves; a heat seeker, an active radar seeker, an anti-radiation round, and a boost motor with a `<Stage>`.

- **Parts:** `ExampleCopy_Prefab_AmraamRail`, `ExampleCopy_Prefab_HarmRail`, `ExampleCopy_Prefab_SidewinderRail`, in `ExampleCopyAssets.xml` and `ExampleCopyGameData.xml`
- **Meshes:** `Meshes/ExampleCopy_Amraam.glb`, `Meshes/ExampleCopy_Harm.glb`, `Meshes/ExampleCopy_MeshAtlas.glb`
- **Textures:** `Textures/ExampleCopy_Amraam_Diffuse.png`, `Textures/ExampleCopy_Amraam_Normal.png`, `Textures/ExampleCopy_Amraam_PBR.png`, `Textures/ExampleCopy_Diffuse.png`, `Textures/ExampleCopy_Harm_Diffuse.png`, `Textures/ExampleCopy_Harm_Normal.png`, `Textures/ExampleCopy_Harm_PBR.png`, `Textures/ExampleCopy_Normal.png`, `Textures/ExampleCopy_PBR.png`
- **Sounds it names:** none of its own
- [KSArmory's own file at that commit](https://github.com/LaurensDeV/KSArmory/blob/c138556f35eba603f9de60320a744852f5b3bd57/src/KSArmory/KSArmory/Rails.xml)

### Sensors: [`KSArmory/Sensors.xml`](KSArmory/Sensors.xml)

Sights as their own parts: a mast head, a roll-nod pod (`Gimbal`), and a search set (`<SearchSet>`) whose head turns behind a window.

- **Parts:** `ExampleCopy_Prefab_Irst`, `ExampleCopy_Prefab_Litening`, `ExampleCopy_Prefab_Optic`, in `ExampleCopyAssets.xml` and `ExampleCopyGameData.xml`
- **Meshes:** `Meshes/ExampleCopy_Irst.glb`, `Meshes/ExampleCopy_Litening.glb`, `Meshes/ExampleCopy_MeshAtlas.glb`, `Meshes/ExampleCopy_Rail.glb`
- **Textures:** `Textures/ExampleCopy_Diffuse.png`, `Textures/ExampleCopy_Irst_Diffuse.png`, `Textures/ExampleCopy_Irst_Normal.png`, `Textures/ExampleCopy_Irst_PBR.png`, `Textures/ExampleCopy_Litening_Body_Diffuse.png`, `Textures/ExampleCopy_Litening_Body_Normal.png`, `Textures/ExampleCopy_Litening_Body_PBR.png`, `Textures/ExampleCopy_Litening_Roll_Diffuse.png`, `Textures/ExampleCopy_Litening_Roll_Normal.png`, `Textures/ExampleCopy_Litening_Roll_PBR.png`, `Textures/ExampleCopy_Litening_Window_Diffuse.png`, `Textures/ExampleCopy_Litening_Window_Normal.png`, `Textures/ExampleCopy_Litening_Window_PBR.png`, `Textures/ExampleCopy_Normal.png`, `Textures/ExampleCopy_PBR.png`, `Textures/ExampleCopy_Rail_Diffuse.png`, `Textures/ExampleCopy_Rail_Normal.png`, `Textures/ExampleCopy_Rail_PBR.png`
- **Sounds it names:** none of its own
- [KSArmory's own file at that commit](https://github.com/LaurensDeV/KSArmory/blob/c138556f35eba603f9de60320a744852f5b3bd57/src/KSArmory/KSArmory/Sensors.xml)

### Strategic: [`KSArmory/Strategic.xml`](KSArmory/Strategic.xml)

A store that falls (`HitsTerrain`, a tail kit, a bomb sight) and a ballistic bus: `Guidance`, trim, hops and `<ReleaseSpin>`.

- **Parts:** `ExampleCopy_Prefab_MirvBus`, `ExampleCopy_Prefab_NukeRack`, in `ExampleCopyAssets.xml` and `ExampleCopyGameData.xml`
- **Meshes:** `Meshes/ExampleCopy_B61.glb`, `Meshes/ExampleCopy_PostBoostBus.glb`
- **Textures:** `Textures/ExampleCopy_B61_Diffuse.png`, `Textures/ExampleCopy_B61_Normal.png`, `Textures/ExampleCopy_B61_PBR.png`, `Textures/ExampleCopy_PostBoostBus_Diffuse.png`, `Textures/ExampleCopy_PostBoostBus_Normal.png`, `Textures/ExampleCopy_PostBoostBus_PBR.png`
- **Sounds it names:** none of its own
- [KSArmory's own file at that commit](https://github.com/LaurensDeV/KSArmory/blob/c138556f35eba603f9de60320a744852f5b3bd57/src/KSArmory/KSArmory/Strategic.xml)

Every attribute of a definition is described in KSArmory's `docs/WEAPON-PACKS.md`.
