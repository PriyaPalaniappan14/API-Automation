import os
import json
from jsonschema import validate
from genson import SchemaBuilder
from helpers.common import get_data_file, load_json_as_dict, YospaceQAException


def load_schema(filename: str) -> dict:
    """
    Getting the payload file in the mentioned directory
    """
    _schema_file = get_data_file(f"schemas/{filename}")

    if not os.path.exists(_schema_file):
        raise FileNotFoundError()

    _schema = load_json_as_dict(_schema_file)
    return _schema


def create_schema(filename: str, instance: dict) -> None:
    _builder = SchemaBuilder()
    _builder.add_object(instance)
    _schema = _builder.to_json(indent=4)

    _schema_file = get_data_file(f"schemas/{filename}")
    with open(_schema_file, "w", encoding="utf-8") as _file:
        _file.write(_schema)

    _payload_file = "".join(_schema_file.split(".")[:-1]) + ".actualresult.json"
    with open(_payload_file, "w", encoding="utf-8") as _payload:
        _payload.write(json.dumps(instance, indent=4))


def validate_schema(filename: str, instance: dict) -> None:
    try:
        _schema = load_schema(filename)
    except FileNotFoundError as err:
        create_schema(filename, instance)
        raise YospaceQAException("Missing POST Job Schema. Created!") from err

    validate(instance, _schema)
