from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CognitoIDPAnalyticsConfigurationType(BaseModel):
    ApplicationId: StrictStr | None = None
    ApplicationArn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ExternalId: StrictStr | None = None
    UserDataShared: StrictBool | None = None
