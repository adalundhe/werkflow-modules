from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_directory_config import AppStreamDirectoryConfig


class AppStreamDescribeDirectoryConfigsResponse(BaseModel):
    DirectoryConfigs: list[AppStreamDirectoryConfig] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
