from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_prefix_list import EC2PrefixList


class EC2DescribePrefixListsResponse(BaseModel):
    NextToken: StrictStr | None = None
    PrefixLists: list[EC2PrefixList] | None = None
    ResponseMetadata: dict[str, Any] | None = None
