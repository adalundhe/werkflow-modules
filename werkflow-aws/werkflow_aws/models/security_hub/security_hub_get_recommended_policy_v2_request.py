from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubGetRecommendedPolicyV2Request(BaseModel):
    MetadataUid: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
