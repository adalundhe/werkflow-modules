from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_credential_pair import QuickSightCredentialPair
from .quick_sight_key_pair_credentials import QuickSightKeyPairCredentials
from .quick_sight_o_auth_client_credentials import QuickSightOAuthClientCredentials
from .quick_sight_one_drive_client_credentials import QuickSightOneDriveClientCredentials
from .quick_sight_service_account_credentials import QuickSightServiceAccountCredentials
from .quick_sight_share_point_client_credentials import QuickSightSharePointClientCredentials
from .quick_sight_web_proxy_credentials import QuickSightWebProxyCredentials


class QuickSightDataSourceCredentials(BaseModel):
    CredentialPair: QuickSightCredentialPair | None = None
    CopySourceArn: StrictStr | None = None
    SecretArn: StrictStr | None = None
    KeyPairCredentials: QuickSightKeyPairCredentials | None = None
    WebProxyCredentials: QuickSightWebProxyCredentials | None = None
    OAuthClientCredentials: QuickSightOAuthClientCredentials | None = None
    ServiceAccountCredentials: QuickSightServiceAccountCredentials | None = None
    SharePointClientCredentials: QuickSightSharePointClientCredentials | None = None
    OneDriveClientCredentials: QuickSightOneDriveClientCredentials | None = None
