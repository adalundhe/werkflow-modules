from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexSlotTypeSummary(BaseModel):
    slotTypeId: StrictStr | None = None
    slotTypeName: StrictStr | None = None
    description: StrictStr | None = None
    parentSlotTypeSignature: StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    slotTypeCategory: StrictStr | None = None
