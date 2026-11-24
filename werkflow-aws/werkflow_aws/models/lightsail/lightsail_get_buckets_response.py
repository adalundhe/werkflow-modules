from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_account_level_bpa_sync import LightsailAccountLevelBpaSync
from .lightsail_bucket import LightsailBucket


class LightsailGetBucketsResponse(BaseModel):
    buckets: list[LightsailBucket] | None = None
    nextPageToken: StrictStr | None = None
    accountLevelBpaSync: LightsailAccountLevelBpaSync | None = None
    ResponseMetadata: dict[str, Any] | None = None
