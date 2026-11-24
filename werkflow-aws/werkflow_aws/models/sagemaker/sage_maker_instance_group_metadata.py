from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_capacity_reservation import SageMakerCapacityReservation


class SageMakerInstanceGroupMetadata(BaseModel):
    FailureMessage: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    CapacityReservation: SageMakerCapacityReservation | None = None
    SubnetId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    AmiOverride: StrictStr | None = None
