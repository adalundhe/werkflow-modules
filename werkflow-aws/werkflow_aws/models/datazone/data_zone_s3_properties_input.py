from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneS3PropertiesInput(BaseModel):
    s3Uri: StrictStr
    s3AccessGrantLocationId: StrictStr | None = None
    registerS3AccessGrantLocation: StrictBool | None = None
