from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_capacity_reservation_adjustment_details import EC2CapacityReservationAdjustmentDetails


class EC2ModifyCapacityReservationResponse(BaseModel):
    Return: StrictBool | None = None
    AdjustmentStatus: StrictStr | None = None
    AdjustmentDetails: EC2CapacityReservationAdjustmentDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
