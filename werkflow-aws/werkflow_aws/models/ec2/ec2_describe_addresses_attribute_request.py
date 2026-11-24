from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeAddressesAttributeRequest(BaseModel):
    AllocationIds: list[StrictStr] | None = None
    Attribute: Literal['domain-name'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    DryRun: StrictBool | None = None
