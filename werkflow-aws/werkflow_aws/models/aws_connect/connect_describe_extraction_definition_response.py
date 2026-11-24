from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_extraction_definition import ConnectExtractionDefinition


class ConnectDescribeExtractionDefinitionResponse(BaseModel):
    ExtractionDefinition: ConnectExtractionDefinition | None = None
    ResponseMetadata: dict[str, Any] | None = None
