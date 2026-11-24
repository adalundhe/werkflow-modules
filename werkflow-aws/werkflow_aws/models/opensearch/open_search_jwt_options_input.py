from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchJWTOptionsInput(BaseModel):
    Enabled: StrictBool | None = None
    SubjectKey: StrictStr | None = None
    RolesKey: StrictStr | None = None
    JwksUrl: StrictStr | None = None
    PublicKey: StrictStr | None = None
