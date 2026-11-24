from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneS3PropertiesOutput(BaseModel):
    s3Uri: StrictStr | None = None
    s3AccessGrantLocationId: StrictStr | None = None
    registerS3AccessGrantLocation: StrictBool | None = None
    status: StrictStr | None = None
    errorMessage: StrictStr | None = None
