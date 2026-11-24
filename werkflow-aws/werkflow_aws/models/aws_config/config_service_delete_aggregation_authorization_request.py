from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteAggregationAuthorizationRequest(BaseModel):
    AuthorizedAccountId: StrictStr
    AuthorizedAwsRegion: StrictStr
