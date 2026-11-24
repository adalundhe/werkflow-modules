from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_capacity_reservation_summary import SageMakerCapacityReservationSummary


class SageMakerListCapacityReservationsResponse(BaseModel):
    CapacityReservationSummaries: list[SageMakerCapacityReservationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
