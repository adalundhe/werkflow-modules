from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2RateBasedStatementManagedKeysIPSet(BaseModel):
    IPAddressVersion: StrictStr | None = None
    Addresses: list[StrictStr] | None = None
