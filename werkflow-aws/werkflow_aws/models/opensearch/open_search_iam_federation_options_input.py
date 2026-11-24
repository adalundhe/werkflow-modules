from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchIAMFederationOptionsInput(BaseModel):
    Enabled: StrictBool | None = None
    SubjectKey: StrictStr | None = None
    RolesKey: StrictStr | None = None
