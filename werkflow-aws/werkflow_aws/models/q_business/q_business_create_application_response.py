from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QBusinessCreateApplicationResponse(BaseModel):
    applicationId: StrictStr | None = None
    applicationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
