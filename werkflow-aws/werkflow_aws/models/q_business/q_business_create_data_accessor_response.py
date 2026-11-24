from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QBusinessCreateDataAccessorResponse(BaseModel):
    dataAccessorId: StrictStr | None = None
    idcApplicationArn: StrictStr | None = None
    dataAccessorArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
