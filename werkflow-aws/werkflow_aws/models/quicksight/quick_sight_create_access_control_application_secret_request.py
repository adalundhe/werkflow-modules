from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_client_secret_configuration import QuickSightClientSecretConfiguration


class QuickSightCreateAccessControlApplicationSecretRequest(BaseModel):
    AwsAccountId: StrictStr
    ApplicationId: StrictStr
    ClientSecretConfiguration: QuickSightClientSecretConfiguration
    Description: StrictStr | None = None
