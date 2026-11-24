from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel


class AWSS3PutObjectLockConfigurationResponse(BaseModel):
    RequestCharged: Literal['requester'] | None = None
    ResponseMetadata: dict[str, Any] | None = None
