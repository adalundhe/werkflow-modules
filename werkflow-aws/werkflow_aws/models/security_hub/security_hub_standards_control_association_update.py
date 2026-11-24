from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStandardsControlAssociationUpdate(BaseModel):
    StandardsArn: StrictStr | None = None
    SecurityControlId: StrictStr | None = None
    AssociationStatus: StrictStr | None = None
    UpdatedReason: StrictStr | None = None
