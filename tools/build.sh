#!/usr/bin/env bash
#
# Builds the mod into bin/Release/net10.0, assets included.
#
# The system dotnet is very likely 8.0 and cannot build net10.0 (error NETSDK1045). If you have
# a .NET 10 SDK somewhere else, put it on PATH first -- KSArmory's tools/env.sh does exactly that.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."
[[ -f ../KSArmory/tools/env.sh ]] && source ../KSArmory/tools/env.sh

dotnet build ExampleMod.csproj -c Release "$@"
