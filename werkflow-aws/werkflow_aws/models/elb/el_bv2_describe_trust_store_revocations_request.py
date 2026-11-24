from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2DescribeTrustStoreRevocationsRequest(BaseModel):
    TrustStoreArn: StrictStr
    RevocationIds: list[StrictInt] | None = None
    Marker: StrictStr | None = None
    PageSize: StrictInt | None = None
