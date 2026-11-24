from __future__ import annotations
from pydantic import BaseModel
from .fms_network_acl_entry_set import FMSNetworkAclEntrySet


class FMSNetworkAclCommonPolicy(BaseModel):
    NetworkAclEntrySet: FMSNetworkAclEntrySet | None = None
