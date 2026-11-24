from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_purchase_request import EC2PurchaseRequest


class EC2PurchaseScheduledInstancesRequest(BaseModel):
    PurchaseRequests: list[EC2PurchaseRequest]
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
