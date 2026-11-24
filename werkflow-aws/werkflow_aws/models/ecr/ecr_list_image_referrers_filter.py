from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECRListImageReferrersFilter(BaseModel):
    artifactTypes: list[StrictStr] | None = None
    artifactStatus: Literal['ACTIVE', 'ARCHIVED', 'ACTIVATING', 'ANY'] | None = None
