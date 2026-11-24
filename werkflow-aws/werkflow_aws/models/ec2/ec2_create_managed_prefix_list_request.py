from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_add_prefix_list_entry import EC2AddPrefixListEntry
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateManagedPrefixListRequest(BaseModel):
    PrefixListName: StrictStr
    MaxEntries: StrictInt
    AddressFamily: StrictStr
    DryRun: StrictBool | None = None
    Entries: list[EC2AddPrefixListEntry] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
