from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Ipv6CidrAssociation(BaseModel):
    Ipv6Cidr: StrictStr | None = None
    AssociatedResource: StrictStr | None = None
