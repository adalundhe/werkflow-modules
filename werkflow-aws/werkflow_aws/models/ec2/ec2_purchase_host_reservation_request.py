from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2PurchaseHostReservationRequest(BaseModel):
    HostIdSet: list[StrictStr]
    OfferingId: StrictStr
    ClientToken: StrictStr | None = None
    CurrencyCode: Literal['USD'] | None = None
    LimitPrice: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
