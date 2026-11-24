from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaAwsSsoAuthentication(BaseModel):
    ssoClientId: StrictStr | None = None
