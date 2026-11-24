from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_vpc_connection_properties import QuickSightVpcConnectionProperties


class QuickSightOAuthClientApplicationSummary(BaseModel):
    OAuthClientApplicationId: StrictStr | None = None
    Name: StrictStr | None = None
    OAuthClientAuthenticationType: StrictStr | None = None
    DataSourceType: StrictStr | None = None
    IdentityProviderVpcConnectionProperties: QuickSightVpcConnectionProperties | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Arn: StrictStr | None = None
