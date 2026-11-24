from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsAppSyncGraphQlApiOpenIdConnectConfigDetails(BaseModel):
    AuthTtL: StrictInt | None = None
    ClientId: StrictStr | None = None
    IatTtL: StrictInt | None = None
    Issuer: StrictStr | None = None
