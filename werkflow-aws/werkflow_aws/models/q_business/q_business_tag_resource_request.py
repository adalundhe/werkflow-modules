from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_tag import QBusinessTag


class QBusinessTagResourceRequest(BaseModel):
    resourceARN: StrictStr
    tags: list[QBusinessTag]
