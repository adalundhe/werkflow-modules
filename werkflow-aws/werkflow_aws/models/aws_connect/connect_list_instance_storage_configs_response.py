from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_instance_storage_config import ConnectInstanceStorageConfig


class ConnectListInstanceStorageConfigsResponse(BaseModel):
    StorageConfigs: list[ConnectInstanceStorageConfig] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
