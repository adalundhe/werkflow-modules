from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFrontDescribeFunctionRequest(BaseModel):
    Name: StrictStr
    Stage: Literal['DEVELOPMENT', 'LIVE'] | None = None
