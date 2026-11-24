from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_field import GlueField


class GlueDescribeEntityResponse(BaseModel):
    Fields: list[GlueField] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
