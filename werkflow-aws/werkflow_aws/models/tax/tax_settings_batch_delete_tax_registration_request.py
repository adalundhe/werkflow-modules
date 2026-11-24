from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsBatchDeleteTaxRegistrationRequest(BaseModel):
    accountIds: list[StrictStr]
