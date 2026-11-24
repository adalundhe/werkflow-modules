from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2NetworkInterfaceAssociation(BaseModel):
    AllocationId: StrictStr | None = None
    AssociationId: StrictStr | None = None
    IpOwnerId: StrictStr | None = None
    PublicDnsName: StrictStr | None = None
    PublicIp: StrictStr | None = None
    CustomerOwnedIp: StrictStr | None = None
    CarrierIp: StrictStr | None = None
