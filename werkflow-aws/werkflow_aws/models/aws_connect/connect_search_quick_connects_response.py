from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_quick_connect import ConnectQuickConnect


class ConnectSearchQuickConnectsResponse(BaseModel):
    QuickConnects: list[ConnectQuickConnect] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
