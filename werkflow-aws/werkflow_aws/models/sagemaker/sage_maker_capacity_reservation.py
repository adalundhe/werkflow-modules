from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCapacityReservation(BaseModel):
    Arn: StrictStr | None = None
    Type: StrictStr | None = None
