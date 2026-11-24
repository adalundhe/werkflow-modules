from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGroupProfileSummary(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    status: StrictStr | None = None
    groupName: StrictStr | None = None
    rolePrincipalArn: StrictStr | None = None
    rolePrincipalId: StrictStr | None = None
