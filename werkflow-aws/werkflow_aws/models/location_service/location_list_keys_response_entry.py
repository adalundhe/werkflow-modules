from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .location_api_key_restrictions import LocationApiKeyRestrictions


class LocationListKeysResponseEntry(BaseModel):
    KeyName: StrictStr | None = None
    ExpireTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Restrictions: LocationApiKeyRestrictions | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
