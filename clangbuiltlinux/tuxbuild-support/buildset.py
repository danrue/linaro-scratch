import json
import requests

response = requests.get("https://api.tuxbuild.com/v1/supportmatrix")
matrix = response.json()

buildset = []
for toolchain,architectures in matrix.items():
    if 'clang' not in toolchain:
        continue
    for architecture in architectures:
        buildset.append({
            "toolchain": toolchain,
            "target_arch": architecture,
            "kconfig": "tinyconfig",
        })

print(json.dumps({"sets": [{"name": "all", "builds": buildset}]}, indent=2))
