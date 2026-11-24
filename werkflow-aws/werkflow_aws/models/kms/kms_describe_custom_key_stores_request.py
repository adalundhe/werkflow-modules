from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KMSDescribeCustomKeyStoresRequest(BaseModel):
    CustomKeyStoreId: StrictStr | None = None
    CustomKeyStoreName: StrictStr | None = None
    Limit: StrictInt | None = None
    Marker: StrictStr | None = None
