from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_managed_prefix_list import EC2ManagedPrefixList


class EC2DeleteManagedPrefixListResponse(BaseModel):
    PrefixList: EC2ManagedPrefixList | None = None
    ResponseMetadata: dict[str, Any] | None = None
