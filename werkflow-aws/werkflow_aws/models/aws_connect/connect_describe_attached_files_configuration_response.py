from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_attached_files_configuration import ConnectAttachedFilesConfiguration


class ConnectDescribeAttachedFilesConfigurationResponse(BaseModel):
    AttachedFilesConfiguration: ConnectAttachedFilesConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
