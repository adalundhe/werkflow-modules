from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightExportWithHiddenFieldsOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None
