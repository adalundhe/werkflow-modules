from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_connection_type_brief import GlueConnectionTypeBrief


class GlueListConnectionTypesResponse(BaseModel):
    ConnectionTypes: list[GlueConnectionTypeBrief] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
