from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .fms_network_acl_entry import FMSNetworkAclEntry


class FMSEntryDescription(BaseModel):
    EntryDetail: FMSNetworkAclEntry | None = None
    EntryRuleNumber: StrictInt | None = None
    EntryType: StrictStr | None = None
