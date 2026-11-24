from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2IPSet(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    Description: StrictStr | None = None
    IPAddressVersion: StrictStr | None = None
    Addresses: list[StrictStr] | None = None
