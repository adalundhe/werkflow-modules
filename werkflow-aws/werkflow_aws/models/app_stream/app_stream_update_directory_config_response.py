from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_directory_config import AppStreamDirectoryConfig


class AppStreamUpdateDirectoryConfigResponse(BaseModel):
    DirectoryConfig: AppStreamDirectoryConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
