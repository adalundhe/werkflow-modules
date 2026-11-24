from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2ManagedPrefixList(BaseModel):
    PrefixListId: StrictStr | None = None
    AddressFamily: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    PrefixListArn: StrictStr | None = None
    PrefixListName: StrictStr | None = None
    MaxEntries: StrictInt | None = None
    Version: StrictInt | None = None
    Tags: list[EC2TagModel] | None = None
    OwnerId: StrictStr | None = None
    IpamPrefixListResolverTargetId: StrictStr | None = None
    IpamPrefixListResolverSyncEnabled: StrictBool | None = None
