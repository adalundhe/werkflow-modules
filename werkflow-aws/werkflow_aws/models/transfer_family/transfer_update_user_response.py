from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class TransferUpdateUserResponse(BaseModel):
    ServerId: StrictStr | None = None
    UserName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
