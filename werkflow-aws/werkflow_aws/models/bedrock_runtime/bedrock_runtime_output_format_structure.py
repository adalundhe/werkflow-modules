from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_json_schema_definition import BedrockRuntimeJsonSchemaDefinition


class BedrockRuntimeOutputFormatStructure(BaseModel):
    jsonSchema: BedrockRuntimeJsonSchemaDefinition | None = None
