from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncGoogleOidcConfig(BaseModel):
    ProjectName: StrictStr | None = None
    ProjectNumber: StrictStr | None = None
    IdentityPoolName: StrictStr | None = None
    IdentityProviderName: StrictStr | None = None
