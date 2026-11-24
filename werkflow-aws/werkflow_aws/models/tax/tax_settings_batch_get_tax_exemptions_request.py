from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsBatchGetTaxExemptionsRequest(BaseModel):
    accountIds: list[StrictStr]
