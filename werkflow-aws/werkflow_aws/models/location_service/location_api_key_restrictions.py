from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .location_android_app import LocationAndroidApp
from .location_apple_app import LocationAppleApp


class LocationApiKeyRestrictions(BaseModel):
    AllowActions: list[StrictStr] | None = None
    AllowResources: list[StrictStr] | None = None
    AllowReferers: list[StrictStr] | None = None
    AllowAndroidApps: list[LocationAndroidApp] | None = None
    AllowAppleApps: list[LocationAppleApp] | None = None
