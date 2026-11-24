from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSConnectCustomKeyStoreRequest(BaseModel):
    CustomKeyStoreId: StrictStr
