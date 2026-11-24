from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_provider_user_identifier_type import CognitoIDPProviderUserIdentifierType


class CognitoIDPAdminLinkProviderForUserRequest(BaseModel):
    UserPoolId: StrictStr
    DestinationUser: CognitoIDPProviderUserIdentifierType
    SourceUser: CognitoIDPProviderUserIdentifierType
