from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeMacHostsRequest(BaseModel):
    Filters: list[EC2FilterModel] | None = None
    HostIds: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
