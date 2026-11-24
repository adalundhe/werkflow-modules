from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RemovePrefixListEntry(BaseModel):
    Cidr: StrictStr
