from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_instance_storage_config import ConnectInstanceStorageConfig


class ConnectDescribeInstanceStorageConfigResponse(BaseModel):
    StorageConfig: ConnectInstanceStorageConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
