from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_schema_version_error_item import GlueSchemaVersionErrorItem


class GlueDeleteSchemaVersionsResponse(BaseModel):
    SchemaVersionErrors: list[GlueSchemaVersionErrorItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
