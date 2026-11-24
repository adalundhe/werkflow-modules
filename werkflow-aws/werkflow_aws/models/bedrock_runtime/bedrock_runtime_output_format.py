from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .bedrock_runtime_output_format_structure import BedrockRuntimeOutputFormatStructure


class BedrockRuntimeOutputFormat(BaseModel):
    type: Literal['json_schema']
    structure: BedrockRuntimeOutputFormatStructure
