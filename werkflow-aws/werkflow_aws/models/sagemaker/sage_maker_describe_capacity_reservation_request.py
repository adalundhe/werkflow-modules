from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeCapacityReservationRequest(BaseModel):
    SMCapacityReservationArn: StrictStr
