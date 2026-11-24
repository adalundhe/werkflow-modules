from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .location_api_key_restrictions import LocationApiKeyRestrictions


class LocationUpdateKeyRequest(BaseModel):
    KeyName: StrictStr
    Description: StrictStr | None = None
    ExpireTime: datetime.datetime | StrictStr | None = None
    NoExpiry: StrictBool | None = None
    ForceUpdate: StrictBool | None = None
    Restrictions: LocationApiKeyRestrictions | None = None
