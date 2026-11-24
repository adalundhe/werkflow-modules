from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListFieldLevelEncryptionConfigsRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
