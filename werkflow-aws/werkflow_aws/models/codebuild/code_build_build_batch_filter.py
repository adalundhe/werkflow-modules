from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class CodeBuildBuildBatchFilter(BaseModel):
    status: Literal['SUCCEEDED', 'FAILED', 'FAULT', 'TIMED_OUT', 'IN_PROGRESS', 'STOPPED'] | None = None
