from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class KinesisVideoUpdateStreamStorageConfigurationResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
