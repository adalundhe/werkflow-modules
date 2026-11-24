from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_record import GlueRecord


class GlueGetEntityRecordsResponse(BaseModel):
    Records: list[GlueRecord] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
