from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsAppSyncGraphQlApiUserPoolConfigDetails(BaseModel):
    AppIdClientRegex: StrictStr | None = None
    AwsRegion: StrictStr | None = None
    DefaultAction: StrictStr | None = None
    UserPoolId: StrictStr | None = None
