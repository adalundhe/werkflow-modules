from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ECRLifecyclePolicyPreviewFilter(BaseModel):
    tagStatus: Literal['TAGGED', 'UNTAGGED', 'ANY'] | None = None
