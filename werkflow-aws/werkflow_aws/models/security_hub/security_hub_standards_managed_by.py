from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStandardsManagedBy(BaseModel):
    Company: StrictStr | None = None
    Product: StrictStr | None = None
