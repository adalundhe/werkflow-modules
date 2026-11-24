from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class TaxSettingsBelgiumAdditionalInfo(BaseModel):
    peppolId: StrictStr | None = None
    isMercuriusBoxEnabled: StrictBool | None = None
