from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_capacity_reservation_filter import SageMakerCapacityReservationFilter


class SageMakerListCapacityReservationsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[SageMakerCapacityReservationFilter] | None = None
