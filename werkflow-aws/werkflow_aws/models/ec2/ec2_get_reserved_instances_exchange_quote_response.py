from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_reservation_value import EC2ReservationValue
from .ec2_reserved_instance_reservation_value import EC2ReservedInstanceReservationValue
from .ec2_target_reservation_value import EC2TargetReservationValue


class EC2GetReservedInstancesExchangeQuoteResponse(BaseModel):
    CurrencyCode: StrictStr | None = None
    IsValidExchange: StrictBool | None = None
    OutputReservedInstancesWillExpireAt: datetime.datetime | StrictStr | None = None
    PaymentDue: StrictStr | None = None
    ReservedInstanceValueRollup: EC2ReservationValue | None = None
    ReservedInstanceValueSet: list[EC2ReservedInstanceReservationValue] | None = None
    TargetConfigurationValueRollup: EC2ReservationValue | None = None
    TargetConfigurationValueSet: list[EC2TargetReservationValue] | None = None
    ValidationFailureReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
