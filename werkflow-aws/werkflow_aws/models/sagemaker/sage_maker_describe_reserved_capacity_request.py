from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeReservedCapacityRequest(BaseModel):
    ReservedCapacityArn: StrictStr
