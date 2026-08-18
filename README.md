# KSArmory example mod

A complete KSArmory weapon pack, as small as one can be and still ship a real weapon. It adds a
**Mk 82 bomb rack**: a pylon, a 500 lb bomb, and a bombsight to release it on.

Copy this folder, rename it, replace the art, and edit `Weapons.xml`.

**KSArmory does not know this mod exists.** It scans no folders, reads no manifest and holds no
list of packs. This mod depends on KSArmory and calls it — which is why installing a pack is
nothing but installing a mod.

## All of the code

`ExampleMod.cs`, in full, is one method that reads a file and hands it over:

```csharp
[StarMapBeforeMain]
public void OnLoad()
{
    string here = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location) ?? ".";
    PackResult result = Armoury.Register(File.ReadAllText(Path.Combine(here, "Weapons.xml")), Name);
    foreach (PackFault fault in result.Faults) Console.WriteLine($"{Name}: {fault}");
}
```

Everything else is data.

`Armoury.Register` takes **text**, and that is what makes this buildable by anyone with a .NET SDK
and nothing else. Constructing a `LauncherProfile` in C# would need `double3` from
`Brutal.Core.Numerics` — RocketWerkz's assembly, which cannot be redistributed — so a pack that
built one would need a KSA install to compile. This one references `KSArmory.dll` and
`StarMap.API.dll`, and the loader ships the second.

## What is in the folder

| | |
| --- | --- |
| `mod.toml` | KSA's `assets` list, and the one `ModDependencies` line that makes it a pack |
| `ExampleMod.cs` | the entry point above |
| `Weapons.xml` | **the weapon** — read by KSArmory, never by KSA |
| `ExampleModAssets.xml` | the atlas, the material, the subparts and the part — read by KSA, never by KSArmory |
| `ExampleModGameData.xml` | mass, colliders, editor tags |
| `Meshes/`, `Textures/` | the art |
| `tools/extract-art.py` | how the mesh was lifted out of KSArmory's atlas. Run once; its output is committed |

The split is worth seeing: **`Weapons.xml` is not in `mod.toml`'s `assets` array**, and must not be.
KSA hands every entry in that list to its own asset-bundle loader, so a weapon file named there is
parsed by the wrong reader. KSArmory finds it because this mod passes it in.

A mod shipping only the two `*Assets.xml` files would still put the rack in the editor. It just
would not be a weapon.

## Build and install

```bash
./tools/build.sh      # needs a .NET 10 SDK; the system dotnet is probably 8.0
./tools/deploy.sh     # build, copy into the KSA mods folder, register in manifest.toml
```

Then launch through **StarMap**, not KSA directly.

Registering is the step people miss. KSA writes a newly discovered mod folder into `manifest.toml`
with `enabled = false` and says nothing about it, so dropping the folder in is not enough —
`deploy.sh` writes the entry for exactly this reason.

## When the part does not appear

`<KSA user dir>/Logs/KSArmory.log` names every definition that was refused and why, and once the
world has loaded it also checks that each registered part actually exists and that every subpart
marker resolves to exactly one subpart.

What no log can tell you is that this mod never ran at all — KSArmory cannot report a pack it
never heard from. Check in this order:

1. **Is it enabled in `manifest.toml`?**
2. **Did StarMap load `ExampleMod.dll`?** Its console says which mods loaded, and says nothing
   when `EntryAssembly` names a file that is not there.
3. **Does `KSArmory.log` mention `ExampleMod`?** No mention means `Register` was never reached.
4. **Is the rack in the editor?** If not, the problem is `ExampleModAssets.xml`, not KSArmory.

## Going further

- `KSArmory/docs/WEAPON-PACKS.md` — every attribute a definition may carry, with the reasons.
- `KSArmory/docs/PACK-API-SURFACE.md` — the same contract generated from the code. KSArmory's
  build fails if it moves without being acknowledged.
- `KSArmory/docs/FROM-KSP-MODDING.md` — read first if you have written KSP parts. There is no
  `PartModule` here, and that is why a pack ships a DLL rather than only a config.
- `KSArmory/.claude/skills/ksa-blender/SKILL.md` — the art contract KSA actually enforces, and the
  defects that are invisible outside the game.

## Two traps that are not yours and will still bite you

- **Never remove a `<SubPart>` from a part you have shipped.** KSA pairs a saved part with its
  current definition positionally, so removing one throws out of `Popup.DrawAll` and terminates the
  game on every save holding that part. Adding and renaming are free.
- **Markers match by case-insensitive substring, first hit wins.** `BodyMarker="Mk82"` matches the
  subpart `ExampleMod_Rack_Mk8200`, and would also match a subpart called `Mk82Cover` if one
  existed. KSArmory warns when a marker matches none or more than one.

## Licence

Public domain (CC0). Copy it.

The mesh and textures are lifted from KSArmory, which generates its own art — see
`tools/extract-art.py` for exactly what was taken.
