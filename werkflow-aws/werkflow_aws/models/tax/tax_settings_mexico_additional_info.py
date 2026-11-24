from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsMexicoAdditionalInfo(BaseModel):
    taxRegime: StrictStr | None = None
    taxRegimeFullName: StrictStr | None = None
    cfdiUsageCode: StrictStr | None = None
