from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .media_store_cors_rule import MediaStoreCorsRule


class MediaStoreGetCorsPolicyResponse(BaseModel):
    CorsPolicy: list[MediaStoreCorsRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
