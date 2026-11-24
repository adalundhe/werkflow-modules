from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetDataExportConfigurationRequest(BaseModel):
    domainIdentifier: StrictStr
