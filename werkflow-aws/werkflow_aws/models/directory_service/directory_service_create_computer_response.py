from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .directory_service_computer import DirectoryServiceComputer


class DirectoryServiceCreateComputerResponse(BaseModel):
    Computer: DirectoryServiceComputer | None = None
    ResponseMetadata: dict[str, Any] | None = None
