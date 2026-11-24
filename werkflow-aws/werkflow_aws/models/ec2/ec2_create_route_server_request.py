from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateRouteServerRequest(BaseModel):
    AmazonSideAsn: StrictInt
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    PersistRoutes: Literal['enable', 'disable', 'reset'] | None = None
    PersistRoutesDuration: StrictInt | None = None
    SnsNotificationsEnabled: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
