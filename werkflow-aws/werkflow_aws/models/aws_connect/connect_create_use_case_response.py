from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateUseCaseResponse(BaseModel):
    UseCaseId: StrictStr | None = None
    UseCaseArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
