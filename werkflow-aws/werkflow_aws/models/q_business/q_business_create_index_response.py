from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QBusinessCreateIndexResponse(BaseModel):
    indexId: StrictStr | None = None
    indexArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
