from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAttachedFileError(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    FileId: StrictStr | None = None
