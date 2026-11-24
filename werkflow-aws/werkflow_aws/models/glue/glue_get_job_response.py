from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_job import GlueJob


class GlueGetJobResponse(BaseModel):
    Job: GlueJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
