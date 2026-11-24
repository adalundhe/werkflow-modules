from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_managed_prefix_list import EC2ManagedPrefixList


class EC2DescribeManagedPrefixListsResponse(BaseModel):
    NextToken: StrictStr | None = None
    PrefixLists: list[EC2ManagedPrefixList] | None = None
    ResponseMetadata: dict[str, Any] | None = None
