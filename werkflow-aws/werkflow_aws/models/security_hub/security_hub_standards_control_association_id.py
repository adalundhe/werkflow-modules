from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStandardsControlAssociationId(BaseModel):
    SecurityControlId: StrictStr | None = None
    StandardsArn: StrictStr | None = None
