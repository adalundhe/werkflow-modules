from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRListSecurityConfigurationsRequest(BaseModel):
    Marker: StrictStr | None = None
