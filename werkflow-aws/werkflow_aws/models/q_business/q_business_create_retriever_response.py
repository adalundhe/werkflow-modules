from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QBusinessCreateRetrieverResponse(BaseModel):
    retrieverId: StrictStr | None = None
    retrieverArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
