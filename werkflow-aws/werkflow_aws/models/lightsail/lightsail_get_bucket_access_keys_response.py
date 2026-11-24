from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_access_key import LightsailAccessKey


class LightsailGetBucketAccessKeysResponse(BaseModel):
    accessKeys: list[LightsailAccessKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
