from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_capacity_reservation_preference import SageMakerCapacityReservationPreference


class SageMakerProductionVariantCapacityReservationConfig(BaseModel):
    CapacityReservationPreference: SageMakerCapacityReservationPreference | None = None
    MlReservationArn: StrictStr | None = None
