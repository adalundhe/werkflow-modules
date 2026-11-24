from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_reserved_instance_limit_price import EC2ReservedInstanceLimitPrice


class EC2PurchaseReservedInstancesOfferingRequest(BaseModel):
    InstanceCount: StrictInt
    ReservedInstancesOfferingId: StrictStr
    PurchaseTime: datetime.datetime | StrictStr | None = None
    DryRun: StrictBool | None = None
    LimitPrice: EC2ReservedInstanceLimitPrice | None = None
