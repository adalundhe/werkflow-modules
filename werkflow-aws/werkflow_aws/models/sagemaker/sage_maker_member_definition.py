from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_cognito_member_definition import SageMakerCognitoMemberDefinition
from .sage_maker_oidc_member_definition import SageMakerOidcMemberDefinition


class SageMakerMemberDefinition(BaseModel):
    CognitoMemberDefinition: SageMakerCognitoMemberDefinition | None = None
    OidcMemberDefinition: SageMakerOidcMemberDefinition | None = None
