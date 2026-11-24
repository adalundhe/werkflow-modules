from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_folder import QuickSightFolder


class QuickSightDescribeFolderResponse(BaseModel):
    Status: StrictInt | None = None
    Folder: QuickSightFolder | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
