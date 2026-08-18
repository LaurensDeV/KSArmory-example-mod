#!/usr/bin/env bash
#
# Builds and installs into the KSA mods folder, then registers the mod.
#
# Registering is not optional and not automatic: KSA writes a newly discovered folder into
# manifest.toml with enabled = false, and says nothing. That is the single most common reason a
# pack "does not work".
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."
./tools/build.sh

USER_DIR="${KSA_USER_DIR:-$(../KSArmory/tools/ksa-user-dir.sh)}"
TARGET="$USER_DIR/mods/ExampleMod"

mkdir -p "$TARGET"
cp -r bin/Release/net10.0/. "$TARGET/"
rm -f "$TARGET"/*.pdb
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
