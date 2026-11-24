from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_api_key_restrictions import LocationApiKeyRestrictions


class LocationDescribeKeyResponse(BaseModel):
    Key: StrictStr | None = None
    KeyArn: StrictStr | None = None
    KeyName: StrictStr | None = None
    Restrictions: LocationApiKeyRestrictions | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ExpireTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
