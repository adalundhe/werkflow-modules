from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IdentityStoreAddress(BaseModel):
    StreetAddress: StrictStr | None = None
    Locality: StrictStr | None = None
    Region: StrictStr | None = None
    PostalCode: StrictStr | None = None
    Country: StrictStr | None = None
    Formatted: StrictStr | None = None
    Type: StrictStr | None = None
    Primary: StrictBool | None = None
