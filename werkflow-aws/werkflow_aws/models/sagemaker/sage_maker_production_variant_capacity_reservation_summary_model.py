from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_ec2_capacity_reservation_model import SageMakerEc2CapacityReservationModel


class SageMakerProductionVariantCapacityReservationSummaryModel(BaseModel):
    MlReservationArn: StrictStr | None = None
    CapacityReservationPreference: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    UsedByCurrentEndpoint: StrictInt | None = None
    Ec2CapacityReservations: list[SageMakerEc2CapacityReservationModel] | None = None
