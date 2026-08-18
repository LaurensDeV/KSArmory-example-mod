#!/usr/bin/env bash
#
# Copies the mod into the KSA mods folder and registers it. There is nothing to build.
#
# Registering is not optional and not automatic: KSA writes a newly discovered folder into
# manifest.toml with enabled = false and says nothing, which is the single most common reason a
# pack "does not work". KSArmory reports a disabled pack it can see, but only if it can see it.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

USER_DIR="${KSA_USER_DIR:-$(../KSArmory/tools/ksa-user-dir.sh)}"
TARGET="$USER_DIR/mods/ExampleMod"

mkdir -p "$TARGET"
rm -rf "${TARGET:?}"/*
cp -r mod.toml ExampleModAssets.xml ExampleModGameData.xml KSArmory Meshes Textures "$TARGET/"
echo "installed to $TARGET"

MANIFEST="$USER_DIR/manifest.toml"
if [[ ! -f "$MANIFEST" ]]; then
    echo "warning: no manifest at $MANIFEST -- register the mod by hand" >&2
elif grep -q '^[[:space:]]*id[[:space:]]*=[[:space:]]*"ExampleMod"' "$MANIFEST"; then
    echo "already registered in manifest.toml"
else
    printf '\n[[mods]]\nid = "ExampleMod"\nenabled = true\n' >> "$MANIFEST"
    echo "registered in manifest.toml"
fi
