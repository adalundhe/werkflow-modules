from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightExportToCSVOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None
