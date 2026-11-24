from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListOpenIDConnectProviderTagsRequest(BaseModel):
    OpenIDConnectProviderArn: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
