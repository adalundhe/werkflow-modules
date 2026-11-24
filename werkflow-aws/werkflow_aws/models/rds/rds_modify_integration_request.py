from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSModifyIntegrationRequest(BaseModel):
    IntegrationIdentifier: StrictStr
    IntegrationName: StrictStr | None = None
    DataFilter: StrictStr | None = None
    Description: StrictStr | None = None
