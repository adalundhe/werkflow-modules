from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_security_key import ConnectSecurityKey


class ConnectListSecurityKeysResponse(BaseModel):
    SecurityKeys: list[ConnectSecurityKey] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
