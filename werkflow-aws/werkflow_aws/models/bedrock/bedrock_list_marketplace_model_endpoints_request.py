from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListMarketplaceModelEndpointsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    modelSourceEquals: StrictStr | None = None
