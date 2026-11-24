from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_tag import ConfigServiceTag


class ConfigServicePutAggregationAuthorizationRequest(BaseModel):
    AuthorizedAccountId: StrictStr
    AuthorizedAwsRegion: StrictStr
    Tags: list[ConfigServiceTag] | None = None
