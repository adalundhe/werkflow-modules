from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeleteFolderResponse(BaseModel):
    Status: StrictInt | None = None
    Arn: StrictStr | None = None
    FolderId: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
