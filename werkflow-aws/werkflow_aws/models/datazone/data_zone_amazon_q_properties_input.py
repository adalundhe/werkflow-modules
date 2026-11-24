from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneAmazonQPropertiesInput(BaseModel):
    isEnabled: StrictBool
    profileArn: StrictStr | None = None
    authMode: StrictStr | None = None
