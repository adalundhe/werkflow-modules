from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueOAuth2Credentials(BaseModel):
    UserManagedClientApplicationClientSecret: StrictStr | None = None
    AccessToken: StrictStr | None = None
    RefreshToken: StrictStr | None = None
    JwtToken: StrictStr | None = None
