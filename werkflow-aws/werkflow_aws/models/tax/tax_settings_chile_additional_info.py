from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsChileAdditionalInfo(BaseModel):
    documentType: StrictStr | None = None
    businessActivity: StrictStr | None = None
