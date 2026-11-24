from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_idp_authorizing_config import QuickSightIdpAuthorizingConfig
from .quick_sight_quick_authentication_config import QuickSightQuickAuthenticationConfig


class QuickSightAccessControlApplication(BaseModel):
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Namespace: StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    TenantUrl: StrictStr | None = None
    Description: StrictStr | None = None
    IdcApplicationArn: StrictStr | None = None
    IdpAuthorizingConfiguration: QuickSightIdpAuthorizingConfig | None = None
    QuickAuthenticationConfiguration: QuickSightQuickAuthenticationConfig | None = None
