from __future__ import annotations
from pydantic import BaseModel
from .worklog_composite_key import WorklogCompositeKey


class BulkWorklogKeyRequestBean(BaseModel):
    requests: list[WorklogCompositeKey] | None = None
