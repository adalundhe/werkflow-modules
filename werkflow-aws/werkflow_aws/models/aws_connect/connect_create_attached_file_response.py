from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateAttachedFileResponse(BaseModel):
    FileArn: StrictStr | None = None
    FileId: StrictStr | None = None
    CreationTime: StrictStr | None = None
    FileStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
