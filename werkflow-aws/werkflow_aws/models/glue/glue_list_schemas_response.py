from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_schema_list_item import GlueSchemaListItem


class GlueListSchemasResponse(BaseModel):
    Schemas: list[GlueSchemaListItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
