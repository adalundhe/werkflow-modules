from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .location_api_key_restrictions import LocationApiKeyRestrictions


class LocationCreateKeyRequest(BaseModel):
    KeyName: StrictStr
    Restrictions: LocationApiKeyRestrictions
    Description: StrictStr | None = None
    ExpireTime: datetime.datetime | StrictStr | None = None
    NoExpiry: StrictBool | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
