from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PrefixListAssociation(BaseModel):
    ResourceId: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
