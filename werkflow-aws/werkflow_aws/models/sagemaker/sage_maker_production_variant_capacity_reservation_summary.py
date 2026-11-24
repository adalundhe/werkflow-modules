from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_capacity_reservation_preference import SageMakerCapacityReservationPreference
from .sage_maker_ec2_capacity_reservation import SageMakerEc2CapacityReservation


class SageMakerProductionVariantCapacityReservationSummary(BaseModel):
    MlReservationArn: StrictStr | None = None
    CapacityReservationPreference: SageMakerCapacityReservationPreference | None = None
    TotalInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    UsedByCurrentEndpoint: StrictInt | None = None
    Ec2CapacityReservations: list[SageMakerEc2CapacityReservation] | None = None
