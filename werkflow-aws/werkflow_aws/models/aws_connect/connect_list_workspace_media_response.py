from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_media_item import ConnectMediaItem


class ConnectListWorkspaceMediaResponse(BaseModel):
    Media: list[ConnectMediaItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
