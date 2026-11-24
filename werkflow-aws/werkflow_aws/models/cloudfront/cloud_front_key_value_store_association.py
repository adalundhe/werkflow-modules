from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontKeyValueStoreAssociation(BaseModel):
    KeyValueStoreARN: StrictStr | None = None
