from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_attribute import DirectoryServiceAttribute


class DirectoryServiceComputer(BaseModel):
    ComputerId: StrictStr | None = None
    ComputerName: StrictStr | None = None
    ComputerAttributes: list[DirectoryServiceAttribute] | None = None
