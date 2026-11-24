from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IAMGenerateServiceLastAccessedDetailsRequest(BaseModel):
    Arn: StrictStr
    Granularity: Literal['SERVICE_LEVEL', 'ACTION_LEVEL'] | None = None
