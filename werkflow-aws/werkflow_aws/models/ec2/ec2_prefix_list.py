from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PrefixList(BaseModel):
    Cidrs: list[StrictStr] | None = None
    PrefixListId: StrictStr | None = None
    PrefixListName: StrictStr | None = None
