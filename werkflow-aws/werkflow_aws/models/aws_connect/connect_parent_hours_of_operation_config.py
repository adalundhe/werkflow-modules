from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectParentHoursOfOperationConfig(BaseModel):
    HoursOfOperationId: StrictStr | None = None
