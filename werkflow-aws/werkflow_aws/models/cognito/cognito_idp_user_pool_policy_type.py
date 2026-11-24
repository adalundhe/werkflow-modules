from __future__ import annotations
from pydantic import BaseModel
from .cognito_idp_password_policy_type import CognitoIDPPasswordPolicyType
from .cognito_idp_sign_in_policy_type import CognitoIDPSignInPolicyType


class CognitoIDPUserPoolPolicyType(BaseModel):
    PasswordPolicy: CognitoIDPPasswordPolicyType | None = None
    SignInPolicy: CognitoIDPSignInPolicyType | None = None
