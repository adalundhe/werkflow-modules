from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsNorwayAdditionalInfo(BaseModel):
    taxRegistrationNumberType: StrictStr | None = None
    peppolId: StrictStr | None = None
