from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_api_key_connection_metadata import QuickSightAPIKeyConnectionMetadata
from .quick_sight_authorization_code_grant_metadata import QuickSightAuthorizationCodeGrantMetadata
from .quick_sight_basic_auth_connection_metadata import QuickSightBasicAuthConnectionMetadata
from .quick_sight_client_credentials_grant_metadata import QuickSightClientCredentialsGrantMetadata
from .quick_sight_iam_connection_metadata import QuickSightIAMConnectionMetadata
from .quick_sight_none_connection_metadata import QuickSightNoneConnectionMetadata


class QuickSightAuthenticationMetadata(BaseModel):
    AuthorizationCodeGrantMetadata: QuickSightAuthorizationCodeGrantMetadata | None = None
    ClientCredentialsGrantMetadata: QuickSightClientCredentialsGrantMetadata | None = None
    BasicAuthConnectionMetadata: QuickSightBasicAuthConnectionMetadata | None = None
    ApiKeyConnectionMetadata: QuickSightAPIKeyConnectionMetadata | None = None
    NoneConnectionMetadata: QuickSightNoneConnectionMetadata | None = None
    IamConnectionMetadata: QuickSightIAMConnectionMetadata | None = None
