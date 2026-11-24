from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsSourceS3Location(BaseModel):
    bucket: StrictStr
    key: StrictStr
