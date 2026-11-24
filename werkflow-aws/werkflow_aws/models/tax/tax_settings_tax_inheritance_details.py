from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsTaxInheritanceDetails(BaseModel):
    parentEntityId: StrictStr | None = None
    inheritanceObtainedReason: StrictStr | None = None
