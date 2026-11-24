from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AsnAssociation(BaseModel):
    Asn: StrictStr | None = None
    Cidr: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    State: StrictStr | None = None
