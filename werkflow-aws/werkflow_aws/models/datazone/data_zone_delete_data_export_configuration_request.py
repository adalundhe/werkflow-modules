from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteDataExportConfigurationRequest(BaseModel):
    domainIdentifier: StrictStr
