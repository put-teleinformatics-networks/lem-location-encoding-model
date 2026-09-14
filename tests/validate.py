#!/usr/bin/env python3
# Copyright 2026 Piotr Augustyniak
# SPDX-License-Identifier: Apache-2.0

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]

with (ROOT / "schemas/lem-core.schema.json").open(encoding="utf-8") as handle:
    core = json.load(handle)
with (ROOT / "schemas/lem-emergency-profile.schema.json").open(encoding="utf-8") as handle:
    emergency = json.load(handle)
with (ROOT / "schemas/lem-network-infrastructure-profile.schema.json").open(encoding="utf-8") as handle:
    network = json.load(handle)
with (ROOT / "tests/test-vectors.json").open(encoding="utf-8") as handle:
    vectors = json.load(handle)

schemas = {"core": core, "emergency": emergency, "network": network}
registry = Registry().with_resources(
    (schema["$id"], Resource.from_contents(schema))
    for schema in schemas.values()
)

for schema in schemas.values():
    Draft202012Validator.check_schema(schema)

failures = []
for vector in vectors:
    schema = schemas[vector["schema"]]
    validator = Draft202012Validator(schema, registry=registry)
    actual = validator.is_valid(vector["data"])
    if actual != vector["valid"]:
        failures.append((vector["name"], vector["valid"], actual))

if failures:
    for name, expected, actual in failures:
        print(f"FAIL: {name}: expected valid={expected}, got {actual}")
    raise SystemExit(1)

print(f"PASS: {len(vectors)} of {len(vectors)} LEM test vectors")
