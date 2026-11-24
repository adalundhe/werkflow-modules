from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_job import GlueJob


class GlueBatchGetJobsResponse(BaseModel):
    Jobs: list[GlueJob] | None = None
    JobsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
