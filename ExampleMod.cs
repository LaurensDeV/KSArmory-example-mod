using System;
using System.IO;
using System.Reflection;

using KSArmory;
using StarMap.API;

namespace ExampleMod;

/// <summary>
/// The whole mod. Everything else in this folder is data.
///
/// <para>Registering from <c>[StarMapBeforeMain]</c> rather than a later hook because the
/// catalogue shuts when KSArmory builds its roster, and StarMap runs a dependent mod's entry
/// point well before that.</para>
/// </summary>
[StarMapMod]
public sealed class ExampleMod
{
    private const string Name = "ExampleMod";

    [StarMapBeforeMain]
    public void OnLoad()
    {
        // Our own folder. Nothing KSA-facing is needed to find it, which is what keeps this
        // assembly buildable against KSArmory.dll and StarMap.API.dll alone.
        string here = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location) ?? ".";

        PackResult result = Armoury.Register(
            File.ReadAllText(Path.Combine(here, "Weapons.xml")), Name);

        // KSArmory logs this too. Printing it as well costs nothing and puts the reason in
        // StarMap's console, which is where somebody looks when the part is missing.
        foreach (PackFault fault in result.Faults) Console.WriteLine($"{Name}: {fault}");
    }
}
