from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3InventorySchedule(BaseModel):
    Frequency: StrictStr | None = None
