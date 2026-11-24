from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGenerateRecommendedPolicyV2Request(BaseModel):
    MetadataUid: StrictStr
