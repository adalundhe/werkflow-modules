from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteIntegrationRequest(BaseModel):
    IntegrationIdentifier: StrictStr
