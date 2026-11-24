from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSubscribedIamPrincipal(BaseModel):
    principalArn: StrictStr | None = None
