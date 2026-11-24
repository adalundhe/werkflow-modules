from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaIdpMetadata(BaseModel):
    url: StrictStr | None = None
    xml: StrictStr | None = None
