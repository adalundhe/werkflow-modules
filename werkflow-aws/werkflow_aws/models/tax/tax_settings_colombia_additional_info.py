from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsColombiaAdditionalInfo(BaseModel):
    responsibilityCodes: list[StrictStr] | None = None
    taxpayerTypeCode: StrictStr | None = None
    issueDate: StrictStr | None = None
