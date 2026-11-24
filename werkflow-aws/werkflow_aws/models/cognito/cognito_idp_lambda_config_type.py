from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_custom_email_lambda_version_config_type import CognitoIDPCustomEmailLambdaVersionConfigType
from .cognito_idp_custom_sms_lambda_version_config_type import CognitoIDPCustomSMSLambdaVersionConfigType
from .cognito_idp_inbound_federation_lambda_type import CognitoIDPInboundFederationLambdaType
from .cognito_idp_pre_token_generation_version_config_type import CognitoIDPPreTokenGenerationVersionConfigType


class CognitoIDPLambdaConfigType(BaseModel):
    PreSignUp: StrictStr | None = None
    CustomMessage: StrictStr | None = None
    PostConfirmation: StrictStr | None = None
    PreAuthentication: StrictStr | None = None
    PostAuthentication: StrictStr | None = None
    DefineAuthChallenge: StrictStr | None = None
    CreateAuthChallenge: StrictStr | None = None
    VerifyAuthChallengeResponse: StrictStr | None = None
    PreTokenGeneration: StrictStr | None = None
    UserMigration: StrictStr | None = None
    PreTokenGenerationConfig: CognitoIDPPreTokenGenerationVersionConfigType | None = None
    CustomSMSSender: CognitoIDPCustomSMSLambdaVersionConfigType | None = None
    CustomEmailSender: CognitoIDPCustomEmailLambdaVersionConfigType | None = None
    KMSKeyID: StrictStr | None = None
    InboundFederation: CognitoIDPInboundFederationLambdaType | None = None
