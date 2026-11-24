from __future__ import annotations
from pydantic import BaseModel
from .worklog_key_result import WorklogKeyResult


class BulkWorklogKeyResponseBean(BaseModel):
    worklogs: list[WorklogKeyResult] | None = None
