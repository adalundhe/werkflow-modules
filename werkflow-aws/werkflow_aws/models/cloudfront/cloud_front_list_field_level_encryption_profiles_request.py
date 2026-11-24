from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListFieldLevelEncryptionProfilesRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
