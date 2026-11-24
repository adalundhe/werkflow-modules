from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_auth_config import QuickSightAuthConfig


class QuickSightUpdateActionConnectorRequest(BaseModel):
    AwsAccountId: StrictStr
    ActionConnectorId: StrictStr
    Name: StrictStr
    AuthenticationConfig: QuickSightAuthConfig
    Description: StrictStr | None = None
    VpcConnectionArn: StrictStr | None = None
