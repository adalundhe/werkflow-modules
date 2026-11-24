from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_add_prefix_list_entry import EC2AddPrefixListEntry
from .ec2_remove_prefix_list_entry import EC2RemovePrefixListEntry


class EC2ModifyManagedPrefixListRequest(BaseModel):
    PrefixListId: StrictStr
    DryRun: StrictBool | None = None
    CurrentVersion: StrictInt | None = None
    PrefixListName: StrictStr | None = None
    AddEntries: list[EC2AddPrefixListEntry] | None = None
    RemoveEntries: list[EC2RemovePrefixListEntry] | None = None
    MaxEntries: StrictInt | None = None
    IpamPrefixListResolverSyncEnabled: StrictBool | None = None
