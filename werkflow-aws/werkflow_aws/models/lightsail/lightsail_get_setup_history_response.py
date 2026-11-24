from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_setup_history import LightsailSetupHistory


class LightsailGetSetupHistoryResponse(BaseModel):
    setupHistory: list[LightsailSetupHistory] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
