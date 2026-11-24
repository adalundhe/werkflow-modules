from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TaxSettingsListTaxExemptionsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
