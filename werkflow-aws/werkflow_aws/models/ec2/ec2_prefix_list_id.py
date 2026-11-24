from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PrefixListId(BaseModel):
    Description: StrictStr | None = None
    PrefixListId: StrictStr | None = None
