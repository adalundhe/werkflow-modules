from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTableCellImageSizingConfiguration(BaseModel):
    TableCellImageScalingConfiguration: StrictStr | None = None
