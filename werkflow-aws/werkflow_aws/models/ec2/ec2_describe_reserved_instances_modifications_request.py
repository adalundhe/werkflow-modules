from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeReservedInstancesModificationsRequest(BaseModel):
    ReservedInstancesModificationIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    Filters: list[EC2FilterModel] | None = None
