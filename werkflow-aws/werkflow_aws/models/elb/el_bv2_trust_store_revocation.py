from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2TrustStoreRevocation(BaseModel):
    TrustStoreArn: StrictStr | None = None
    RevocationId: StrictInt | None = None
    RevocationType: StrictStr | None = None
    NumberOfRevokedEntries: StrictInt | None = None
