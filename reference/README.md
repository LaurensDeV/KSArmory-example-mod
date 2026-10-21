# Reference: every KSArmory weapon, its parts and its art

Generated from KSArmory `d9ded3adfb` (2026-10-21) by `tools/export-reference.py` in that repository. Do not edit anything in this folder; it is overwritten.

This folder is laid out as KSArmory's own install without its code: the weapon definitions in `KSArmory/`, the parts KSA reads in `KSArmory*.xml`, and the art in `Meshes/`, `Textures/` and `Sounds/`, so every path in the part XML resolves here. It is here to read, not to load: `tools/deploy.sh` does not install it, and it declares KSArmory's own part Ids, so installed as a mod beside KSArmory every one of them would collide.

To start from a weapon, copy its definitions into a file in your mod's `KSArmory/` folder. Any `.xml` there is read and the file name is yours to choose. **Change every `PartId` to a part your mod declares**, or switch that family off under KSArmory > Built-in weapons to replace it on KSArmory's own part: while the family is on, its parts are taken and a second definition is refused. A `Name` can stay as it is, because a pack's names are its own (`YourMod:20MM`); a reference to one of KSArmory's is written `KSArmory:20MM`, which also lets a pack use its rounds and sensors without copying them.

Copying a part means its `<SubPart>` templates, its `<Part>`, its `<PartGameData>`, and the atlas and materials they name, all under Ids of your own; a marker a definition names is the Id the `<Part>` gives a subpart, not the template's. A gun naming no sound plays `KSArmoryCannon`.

## By family

### Countermeasures: [`KSArmory/Countermeasures.xml`](KSArmory/Countermeasures.xml)

`<Decoy>` and `<Dispenser>`: one kind of decoy per part.

- **Parts:** `KSArmory_Prefab_Ale47Chaff`, `KSArmory_Prefab_Ale47Flare`, declared in `KSArmoryAssets.xml` and `KSArmoryGameData.xml`
- **Meshes:** `Meshes/KSArmory_Ale47.glb`
- **Textures:** `Textures/KSArmory_Ale47_Diffuse.png`, `Textures/KSArmory_Ale47_Normal.png`, `Textures/KSArmory_Ale47_PBR.png`
- **Sounds it names:** none of its own
- [The live file at that commit](https://github.com/LaurensDeV/KSArmory/blob/d9ded3adfb828609698bd46d74d16ac89ce91c9e/src/KSArmory/KSArmory/Countermeasures.xml)

### DirectedEnergy: [`KSArmory/DirectedEnergy.xml`](KSArmory/DirectedEnergy.xml)

A beam weapon: `<Beam>` inside an `<Optic>`, and a `<Launcher>` with `FiresBeam` and no round.

- **Parts:** `KSArmory_Prefab_Yal1Turret`, declared in `KSArmoryAssets.xml` and `KSArmoryGameData.xml`
- **Meshes:** `Meshes/KSArmory_Yal1.glb`
- **Textures:** `Textures/KSArmory_Yal1_Diffuse.png`, `Textures/KSArmory_Yal1_Normal.png`, `Textures/KSArmory_Yal1_PBR.png`
- **Sounds it names:** none of its own
- [The live file at that commit](https://github.com/LaurensDeV/KSArmory/blob/d9ded3adfb828609698bd46d74d16ac89ce91c9e/src/KSArmory/KSArmory/DirectedEnergy.xml)

### Guns: [`KSArmory/Guns.xml`](KSArmory/Guns.xml)

Guns with no tubes: `<Muzzle>`, belts and bursts, a rotary cluster, a time-fuzed shell, a chin turret's travel limit, and the cylinder and rod drawn on its linkage.

- **Parts:** `KSArmory_Prefab_Ciws`, `KSArmory_Prefab_M197`, `KSArmory_Prefab_Mk42`, declared in `KSArmoryAssets.xml` and `KSArmoryGameData.xml`
- **Meshes:** `Meshes/KSArmory_Ciws.glb`, `Meshes/KSArmory_M197.glb`, `Meshes/KSArmory_Mk42.glb`
- **Textures:** `Textures/KSArmory_Ciws_Diffuse.png`, `Textures/KSArmory_Ciws_Normal.png`, `Textures/KSArmory_Ciws_PBR.png`, `Textures/KSArmory_M197_Diffuse.png`, `Textures/KSArmory_M197_Normal.png`, `Textures/KSArmory_M197_PBR.png`, `Textures/KSArmory_Mk42Shell_Diffuse.png`, `Textures/KSArmory_Mk42Shell_Normal.png`, `Textures/KSArmory_Mk42Shell_PBR.png`, `Textures/KSArmory_Mk42_Diffuse.png`, `Textures/KSArmory_Mk42_Normal.png`, `Textures/KSArmory_Mk42_PBR.png`
- **Sounds it names:** `Sounds/KSArmory_M197_Loop.wav`, `Sounds/KSArmory_M197_Tail.wav`, `Sounds/KSArmory_Mk42_Gunshot.wav`
- [The live file at that commit](https://github.com/LaurensDeV/KSArmory/blob/d9ded3adfb828609698bd46d74d16ac89ce91c9e/src/KSArmory/KSArmory/Guns.xml)

### Pantsir: [`KSArmory/Pantsir.xml`](KSArmory/Pantsir.xml)

A launcher that traverses and elevates, twelve tubes in two pods, a cannon on the same traverse, and a director on its roof (`<Optic>` beside a `<Launcher>` on one part).

- **Parts:** `KSArmory_Prefab_Launcher6`, declared in `KSArmoryAssets.xml` and `KSArmoryGameData.xml`
- **Meshes:** `Meshes/KSArmory_MeshAtlas.glb`
- **Textures:** `Textures/KSArmory_Diffuse.png`, `Textures/KSArmory_Normal.png`, `Textures/KSArmory_PBR.png`
- **Sounds it names:** none of its own
- [The live file at that commit](https://github.com/LaurensDeV/KSArmory/blob/d9ded3adfb828609698bd46d74d16ac89ce91c9e/src/KSArmory/KSArmory/Pantsir.xml)

### Rails: [`KSArmory/Rails.xml`](KSArmory/Rails.xml)

A launcher with nothing that moves; a heat seeker, an active radar seeker, an anti-radiation round, and a boost motor with a `<Stage>`.

- **Parts:** `KSArmory_Prefab_AmraamRail`, `KSArmory_Prefab_HarmRail`, `KSArmory_Prefab_SidewinderRail`, declared in `KSArmoryAssets.xml` and `KSArmoryGameData.xml`
- **Meshes:** `Meshes/KSArmory_Amraam.glb`, `Meshes/KSArmory_Harm.glb`, `Meshes/KSArmory_MeshAtlas.glb`
- **Textures:** `Textures/KSArmory_Amraam_Diffuse.png`, `Textures/KSArmory_Amraam_Normal.png`, `Textures/KSArmory_Amraam_PBR.png`, `Textures/KSArmory_Diffuse.png`, `Textures/KSArmory_Harm_Diffuse.png`, `Textures/KSArmory_Harm_Normal.png`, `Textures/KSArmory_Harm_PBR.png`, `Textures/KSArmory_Normal.png`, `Textures/KSArmory_PBR.png`
- **Sounds it names:** none of its own
- [The live file at that commit](https://github.com/LaurensDeV/KSArmory/blob/d9ded3adfb828609698bd46d74d16ac89ce91c9e/src/KSArmory/KSArmory/Rails.xml)

### Sensors: [`KSArmory/Sensors.xml`](KSArmory/Sensors.xml)

Sights as their own parts: a mast head, a roll-nod pod (`Gimbal`), and a search set (`<SearchSet>`) whose head turns behind a window.

- **Parts:** `KSArmory_Prefab_Irst`, `KSArmory_Prefab_Litening`, `KSArmory_Prefab_Optic`, declared in `KSArmoryAssets.xml` and `KSArmoryGameData.xml`
- **Meshes:** `Meshes/KSArmory_Irst.glb`, `Meshes/KSArmory_Litening.glb`, `Meshes/KSArmory_MeshAtlas.glb`, `Meshes/KSArmory_Rail.glb`
- **Textures:** `Textures/KSArmory_Diffuse.png`, `Textures/KSArmory_Irst_Diffuse.png`, `Textures/KSArmory_Irst_Normal.png`, `Textures/KSArmory_Irst_PBR.png`, `Textures/KSArmory_Litening_Body_Diffuse.png`, `Textures/KSArmory_Litening_Body_Normal.png`, `Textures/KSArmory_Litening_Body_PBR.png`, `Textures/KSArmory_Litening_Roll_Diffuse.png`, `Textures/KSArmory_Litening_Roll_Normal.png`, `Textures/KSArmory_Litening_Roll_PBR.png`, `Textures/KSArmory_Litening_Window_Diffuse.png`, `Textures/KSArmory_Litening_Window_Normal.png`, `Textures/KSArmory_Litening_Window_PBR.png`, `Textures/KSArmory_Normal.png`, `Textures/KSArmory_PBR.png`, `Textures/KSArmory_Rail_Diffuse.png`, `Textures/KSArmory_Rail_Normal.png`, `Textures/KSArmory_Rail_PBR.png`
- **Sounds it names:** none of its own
- [The live file at that commit](https://github.com/LaurensDeV/KSArmory/blob/d9ded3adfb828609698bd46d74d16ac89ce91c9e/src/KSArmory/KSArmory/Sensors.xml)

### Strategic: [`KSArmory/Strategic.xml`](KSArmory/Strategic.xml)

A store that falls (`HitsTerrain`, a tail kit, a bomb sight) and a ballistic bus: `Guidance`, trim, hops and `<ReleaseSpin>`.

- **Parts:** `KSArmory_Prefab_MirvBus`, `KSArmory_Prefab_NukeRack`, declared in `KSArmoryAssets.xml` and `KSArmoryGameData.xml`
- **Meshes:** `Meshes/KSArmory_B61.glb`, `Meshes/KSArmory_PostBoostBus.glb`
- **Textures:** `Textures/KSArmory_B61_Diffuse.png`, `Textures/KSArmory_B61_Normal.png`, `Textures/KSArmory_B61_PBR.png`, `Textures/KSArmory_PostBoostBus_Diffuse.png`, `Textures/KSArmory_PostBoostBus_Normal.png`, `Textures/KSArmory_PostBoostBus_PBR.png`
- **Sounds it names:** none of its own
- [The live file at that commit](https://github.com/LaurensDeV/KSArmory/blob/d9ded3adfb828609698bd46d74d16ac89ce91c9e/src/KSArmory/KSArmory/Strategic.xml)

Every attribute of a definition is described in KSArmory's `docs/WEAPON-PACKS.md`.
