from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_tota_update_summary import IoTOTAUpdateSummary


class IoTListOTAUpdatesResponse(BaseModel):
    otaUpdates: list[IoTOTAUpdateSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
