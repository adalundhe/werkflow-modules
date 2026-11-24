from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateIpamPrefixListResolverTargetRequest(BaseModel):
    IpamPrefixListResolverId: StrictStr
    PrefixListId: StrictStr
    PrefixListRegion: StrictStr
    TrackLatestVersion: StrictBool
    DryRun: StrictBool | None = None
    DesiredVersion: StrictInt | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
