from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2IpamResourceDiscoveryAssociation(BaseModel):
    OwnerId: StrictStr | None = None
    IpamResourceDiscoveryAssociationId: StrictStr | None = None
    IpamResourceDiscoveryAssociationArn: StrictStr | None = None
    IpamResourceDiscoveryId: StrictStr | None = None
    IpamId: StrictStr | None = None
    IpamArn: StrictStr | None = None
    IpamRegion: StrictStr | None = None
    IsDefault: StrictBool | None = None
    ResourceDiscoveryStatus: StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
