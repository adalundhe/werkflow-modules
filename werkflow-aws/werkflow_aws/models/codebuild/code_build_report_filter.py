from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class CodeBuildReportFilter(BaseModel):
    status: Literal['GENERATING', 'SUCCEEDED', 'FAILED', 'INCOMPLETE', 'DELETING'] | None = None
