from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateHoursOfOperationResponse(BaseModel):
    HoursOfOperationId: StrictStr | None = None
    HoursOfOperationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
