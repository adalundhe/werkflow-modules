from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationValidateAddressActionOptions(BaseModel):
    AdditionalFeatures: list[StrictStr] | None = None
