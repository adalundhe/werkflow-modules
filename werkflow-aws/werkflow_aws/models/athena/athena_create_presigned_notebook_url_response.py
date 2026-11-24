from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaCreatePresignedNotebookUrlResponse(BaseModel):
    NotebookUrl: StrictStr | None = None
    AuthToken: StrictStr | None = None
    AuthTokenExpirationTime: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
