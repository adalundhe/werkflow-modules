from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2TrustStore(BaseModel):
    Name: StrictStr | None = None
    TrustStoreArn: StrictStr | None = None
    Status: StrictStr | None = None
    NumberOfCaCertificates: StrictInt | None = None
    TotalRevokedEntries: StrictInt | None = None
