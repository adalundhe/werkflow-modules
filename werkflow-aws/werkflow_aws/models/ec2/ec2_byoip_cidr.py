from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_asn_association import EC2AsnAssociation


class EC2ByoipCidr(BaseModel):
    Cidr: StrictStr | None = None
    Description: StrictStr | None = None
    AsnAssociations: list[EC2AsnAssociation] | None = None
    StatusMessage: StrictStr | None = None
    State: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    AdvertisementType: StrictStr | None = None
    PoolId: StrictStr | None = None
    IpamPoolId: StrictStr | None = None
