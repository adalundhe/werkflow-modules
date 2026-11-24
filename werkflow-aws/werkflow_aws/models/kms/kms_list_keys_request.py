from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KMSListKeysRequest(BaseModel):
    Limit: StrictInt | None = None
    Marker: StrictStr | None = None
    ResourceOwners: list[Literal['SELF', 'OTHER_ACCOUNTS_VIA_RAM']] | None = None
