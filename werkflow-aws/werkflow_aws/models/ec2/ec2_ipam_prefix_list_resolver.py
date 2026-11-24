from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2IpamPrefixListResolver(BaseModel):
    OwnerId: StrictStr | None = None
    IpamPrefixListResolverId: StrictStr | None = None
    IpamPrefixListResolverArn: StrictStr | None = None
    IpamArn: StrictStr | None = None
    IpamRegion: StrictStr | None = None
    Description: StrictStr | None = None
    AddressFamily: StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    LastVersionCreationStatus: StrictStr | None = None
    LastVersionCreationStatusMessage: StrictStr | None = None
