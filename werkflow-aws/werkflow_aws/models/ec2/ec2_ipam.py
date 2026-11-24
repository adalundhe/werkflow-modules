from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ipam_operating_region import EC2IpamOperatingRegion
from .ec2_tag_model import EC2TagModel


class EC2Ipam(BaseModel):
    OwnerId: StrictStr | None = None
    IpamId: StrictStr | None = None
    IpamArn: StrictStr | None = None
    IpamRegion: StrictStr | None = None
    PublicDefaultScopeId: StrictStr | None = None
    PrivateDefaultScopeId: StrictStr | None = None
    ScopeCount: StrictInt | None = None
    Description: StrictStr | None = None
    OperatingRegions: list[EC2IpamOperatingRegion] | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    DefaultResourceDiscoveryId: StrictStr | None = None
    DefaultResourceDiscoveryAssociationId: StrictStr | None = None
    ResourceDiscoveryAssociationCount: StrictInt | None = None
    StateMessage: StrictStr | None = None
    Tier: StrictStr | None = None
    EnablePrivateGua: StrictBool | None = None
    MeteredAccount: StrictStr | None = None
