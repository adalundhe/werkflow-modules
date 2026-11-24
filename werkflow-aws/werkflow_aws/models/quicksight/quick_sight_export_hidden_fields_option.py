from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightExportHiddenFieldsOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None
