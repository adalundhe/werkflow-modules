from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_lag import DirectConnectLag


class DirectConnectDescribeLagsResponse(BaseModel):
    lags: list[DirectConnectLag] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
