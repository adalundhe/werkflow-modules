from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PrefixListEntry(BaseModel):
    Cidr: StrictStr | None = None
    Description: StrictStr | None = None
