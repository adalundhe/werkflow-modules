from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_job_bookmark_entry import GlueJobBookmarkEntry


class GlueGetJobBookmarkResponse(BaseModel):
    JobBookmarkEntry: GlueJobBookmarkEntry | None = None
    ResponseMetadata: dict[str, Any] | None = None
