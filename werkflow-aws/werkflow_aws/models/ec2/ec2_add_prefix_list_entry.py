from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AddPrefixListEntry(BaseModel):
    Cidr: StrictStr
    Description: StrictStr | None = None
