from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchIdentityCenterOptions(BaseModel):
    EnabledAPIAccess: StrictBool | None = None
    IdentityCenterInstanceARN: StrictStr | None = None
    IdentityCenterInstanceRegion: StrictStr | None = None
    SubjectKey: StrictStr | None = None
    RolesKey: StrictStr | None = None
    IdentityCenterApplicationARN: StrictStr | None = None
    IdentityStoreId: StrictStr | None = None
