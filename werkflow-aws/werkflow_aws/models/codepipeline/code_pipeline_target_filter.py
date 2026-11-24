from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineTargetFilter(BaseModel):
    name: Literal['TARGET_STATUS'] | None = None
    values: list[StrictStr] | None = None
