from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_end_point_type import LambdaEndPointType


class LambdaSelfManagedEventSource(BaseModel):
    Endpoints: dict[LambdaEndPointType, list[StrictStr]] | None = None
