from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2IpamInternetRegistryAssociation(BaseModel):
    OwnerId: StrictStr | None = None
    IpamInternetRegistryAssociationId: StrictStr | None = None
    IpamInternetRegistryAssociationArn: StrictStr | None = None
    IpamId: StrictStr | None = None
    IpamRegion: StrictStr | None = None
    Rir: StrictStr | None = None
    OrganizationHandle: StrictStr | None = None
    Description: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    ChildRequestXml: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
