from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_radius_settings import DirectoryServiceRadiusSettings


class DirectoryServiceUpdateRadiusRequest(BaseModel):
    DirectoryId: StrictStr
    RadiusSettings: DirectoryServiceRadiusSettings
