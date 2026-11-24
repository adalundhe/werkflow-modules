from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSubscribedIamPrincipalInput(BaseModel):
    identifier: StrictStr | None = None
