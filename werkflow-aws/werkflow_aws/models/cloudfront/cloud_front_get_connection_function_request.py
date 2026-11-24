from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFrontGetConnectionFunctionRequest(BaseModel):
    Identifier: StrictStr
    Stage: Literal['DEVELOPMENT', 'LIVE'] | None = None
