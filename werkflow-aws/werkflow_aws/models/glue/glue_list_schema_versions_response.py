from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_schema_version_list_item import GlueSchemaVersionListItem


class GlueListSchemaVersionsResponse(BaseModel):
    Schemas: list[GlueSchemaVersionListItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
