from __future__ import annotations
from pydantic import BaseModel
from .connect_allowed_extension import ConnectAllowedExtension


class ConnectExtensionConfiguration(BaseModel):
    AllowedExtensions: list[ConnectAllowedExtension] | None = None
