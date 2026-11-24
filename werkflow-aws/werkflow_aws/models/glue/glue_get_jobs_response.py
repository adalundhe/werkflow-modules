from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_job import GlueJob


class GlueGetJobsResponse(BaseModel):
    Jobs: list[GlueJob] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
