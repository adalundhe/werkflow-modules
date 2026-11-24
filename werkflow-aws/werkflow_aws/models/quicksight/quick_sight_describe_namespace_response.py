from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_namespace_info_v2 import QuickSightNamespaceInfoV2


class QuickSightDescribeNamespaceResponse(BaseModel):
    Namespace: QuickSightNamespaceInfoV2 | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
