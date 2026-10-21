# Reference: every KSArmory weapon as a pack declares it

Generated from KSArmory `eecf7bd8e7` (2026-10-21) by `tools/export-reference.py` in that repository. Do not edit these files; they are overwritten.

These are KSArmory's own weapon definitions, in the same format as `../KSArmory/Weapons.xml`. They are here to read, not to load: KSArmory reads only the `KSArmory/` folder, so nothing in this one registers.

To start from one, copy the definitions you want into a file in your mod's `KSArmory/` folder. Any `.xml` there is read and the file name is yours to choose. **Change every `PartId` to a part your mod declares**, or switch that family off under KSArmory > Built-in weapons to replace it on KSArmory's own part: while the family is on, its parts are taken and a second definition is refused. A `Name` can stay as it is, because a pack's names are its own (`YourMod:20MM`); a reference to one of KSArmory's is written `KSArmory:20MM`, which also lets a pack use its rounds and sensors without copying them.

| File | What it shows | At that commit |
| --- | --- | --- |
| [`Countermeasures.xml`](Countermeasures.xml) | `<Decoy>` and `<Dispenser>`: one kind of decoy per part | [live](https://github.com/LaurensDeV/KSArmory/blob/eecf7bd8e78e8759ce690dedfb0b016ae009712f/src/KSArmory/KSArmory/Countermeasures.xml) |
| [`DirectedEnergy.xml`](DirectedEnergy.xml) | a beam weapon: `<Beam>` inside an `<Optic>`, and a `<Launcher>` with `FiresBeam` and no round | [live](https://github.com/LaurensDeV/KSArmory/blob/eecf7bd8e78e8759ce690dedfb0b016ae009712f/src/KSArmory/KSArmory/DirectedEnergy.xml) |
| [`Guns.xml`](Guns.xml) | guns with no tubes: `<Muzzle>`, belts and bursts, a rotary cluster, a time-fuzed shell, a chin turret's travel limit, and the cylinder and rod drawn on its linkage | [live](https://github.com/LaurensDeV/KSArmory/blob/eecf7bd8e78e8759ce690dedfb0b016ae009712f/src/KSArmory/KSArmory/Guns.xml) |
| [`Pantsir.xml`](Pantsir.xml) | a launcher that traverses and elevates, twelve tubes in two pods, a cannon on the same traverse, and a director on its roof (`<Optic>` beside a `<Launcher>` on one part) | [live](https://github.com/LaurensDeV/KSArmory/blob/eecf7bd8e78e8759ce690dedfb0b016ae009712f/src/KSArmory/KSArmory/Pantsir.xml) |
| [`Rails.xml`](Rails.xml) | a launcher with nothing that moves; a heat seeker, an active radar seeker, an anti-radiation round, and a boost motor with a `<Stage>` | [live](https://github.com/LaurensDeV/KSArmory/blob/eecf7bd8e78e8759ce690dedfb0b016ae009712f/src/KSArmory/KSArmory/Rails.xml) |
| [`Sensors.xml`](Sensors.xml) | sights as their own parts: a mast head, a roll-nod pod (`Gimbal`), and a search set (`<SearchSet>`) whose head turns behind a window | [live](https://github.com/LaurensDeV/KSArmory/blob/eecf7bd8e78e8759ce690dedfb0b016ae009712f/src/KSArmory/KSArmory/Sensors.xml) |
| [`Strategic.xml`](Strategic.xml) | a store that falls (`HitsTerrain`, a tail kit, a bomb sight) and a ballistic bus: `Guidance`, trim, hops and `<ReleaseSpin>` | [live](https://github.com/LaurensDeV/KSArmory/blob/eecf7bd8e78e8759ce690dedfb0b016ae009712f/src/KSArmory/KSArmory/Strategic.xml) |

Every attribute is described in KSArmory's `docs/WEAPON-PACKS.md`.
