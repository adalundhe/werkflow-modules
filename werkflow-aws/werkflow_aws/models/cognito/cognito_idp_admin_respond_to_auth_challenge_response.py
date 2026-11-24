from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_authentication_result_type import CognitoIDPAuthenticationResultType


class CognitoIDPAdminRespondToAuthChallengeResponse(BaseModel):
    ChallengeName: StrictStr | None = None
    Session: StrictStr | None = None
    ChallengeParameters: dict[StrictStr, StrictStr] | None = None
    AuthenticationResult: CognitoIDPAuthenticationResultType | None = None
    AvailableChallenges: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
