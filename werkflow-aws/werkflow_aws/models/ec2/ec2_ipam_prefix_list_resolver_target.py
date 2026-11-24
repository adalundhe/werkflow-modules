from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2IpamPrefixListResolverTarget(BaseModel):
    IpamPrefixListResolverTargetId: StrictStr | None = None
    IpamPrefixListResolverTargetArn: StrictStr | None = None
    IpamPrefixListResolverId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    PrefixListId: StrictStr | None = None
    PrefixListRegion: StrictStr | None = None
    DesiredVersion: StrictInt | None = None
    LastSyncedVersion: StrictInt | None = None
    TrackLatestVersion: StrictBool | None = None
    StateMessage: StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
