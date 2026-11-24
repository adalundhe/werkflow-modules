from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsDestinationS3Location(BaseModel):
    bucket: StrictStr
    prefix: StrictStr | None = None
