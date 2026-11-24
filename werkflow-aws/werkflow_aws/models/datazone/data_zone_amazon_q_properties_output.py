from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneAmazonQPropertiesOutput(BaseModel):
    isEnabled: StrictBool | None = None
    profileArn: StrictStr | None = None
    authMode: StrictStr | None = None
