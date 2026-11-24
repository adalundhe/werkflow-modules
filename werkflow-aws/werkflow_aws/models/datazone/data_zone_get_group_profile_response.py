from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneGetGroupProfileResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    status: StrictStr | None = None
    groupName: StrictStr | None = None
    rolePrincipalArn: StrictStr | None = None
    rolePrincipalId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
