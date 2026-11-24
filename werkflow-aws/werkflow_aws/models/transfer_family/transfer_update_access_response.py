from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class TransferUpdateAccessResponse(BaseModel):
    ServerId: StrictStr | None = None
    ExternalId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
