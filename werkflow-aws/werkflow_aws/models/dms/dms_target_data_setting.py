from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSTargetDataSetting(BaseModel):
    TablePreparationMode: StrictStr | None = None
