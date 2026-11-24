from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerEc2CapacityReservationModel(BaseModel):
    Ec2CapacityReservationId: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    UsedByCurrentEndpoint: StrictInt | None = None
