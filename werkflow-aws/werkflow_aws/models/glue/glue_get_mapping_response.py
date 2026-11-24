from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_mapping_entry import GlueMappingEntry


class GlueGetMappingResponse(BaseModel):
    Mapping: list[GlueMappingEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
