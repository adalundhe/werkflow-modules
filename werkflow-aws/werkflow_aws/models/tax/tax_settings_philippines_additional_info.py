from __future__ import annotations
from pydantic import BaseModel, StrictBool


class TaxSettingsPhilippinesAdditionalInfo(BaseModel):
    isVatRegistered: StrictBool | None = None
