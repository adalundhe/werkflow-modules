from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_idp_authorizing_config_summary import QuickSightIdpAuthorizingConfigSummary
from .quick_sight_quick_authentication_config import QuickSightQuickAuthenticationConfig


class QuickSightAccessControlApplicationSummary(BaseModel):
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Namespace: StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    TenantUrl: StrictStr | None = None
    IdpAuthorizingConfiguration: QuickSightIdpAuthorizingConfigSummary | None = None
    QuickAuthenticationConfiguration: QuickSightQuickAuthenticationConfig | None = None
    Description: StrictStr | None = None
