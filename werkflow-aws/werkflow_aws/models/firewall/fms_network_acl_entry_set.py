from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .fms_network_acl_entry import FMSNetworkAclEntry


class FMSNetworkAclEntrySet(BaseModel):
    FirstEntries: list[FMSNetworkAclEntry] | None = None
    ForceRemediateForFirstEntries: StrictBool | None = None
    LastEntries: list[FMSNetworkAclEntry] | None = None
    ForceRemediateForLastEntries: StrictBool | None = None
