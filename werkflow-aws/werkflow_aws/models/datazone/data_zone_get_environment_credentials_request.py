from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetEnvironmentCredentialsRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
