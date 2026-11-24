from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListSAMLProviderTagsRequest(BaseModel):
    SAMLProviderArn: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
