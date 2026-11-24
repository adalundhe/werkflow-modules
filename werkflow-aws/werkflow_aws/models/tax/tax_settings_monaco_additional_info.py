from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsMonacoAdditionalInfo(BaseModel):
    businessNumber: StrictStr | None = None
