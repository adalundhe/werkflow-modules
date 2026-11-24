from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_tota_update_info import IoTOTAUpdateInfo


class IoTGetOTAUpdateResponse(BaseModel):
    otaUpdateInfo: IoTOTAUpdateInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
