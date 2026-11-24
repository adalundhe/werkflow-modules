from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateUserResponse(BaseModel):
    UserId: StrictStr | None = None
    UserArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
