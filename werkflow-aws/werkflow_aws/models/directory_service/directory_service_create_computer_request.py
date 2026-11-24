from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_attribute import DirectoryServiceAttribute


class DirectoryServiceCreateComputerRequest(BaseModel):
    DirectoryId: StrictStr
    ComputerName: StrictStr
    Password: StrictStr
    OrganizationalUnitDistinguishedName: StrictStr | None = None
    ComputerAttributes: list[DirectoryServiceAttribute] | None = None
