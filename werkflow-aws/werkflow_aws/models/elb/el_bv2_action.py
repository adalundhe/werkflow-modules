from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .el_bv2_authenticate_cognito_action_config import ELBv2AuthenticateCognitoActionConfig
from .el_bv2_authenticate_oidc_action_config import ELBv2AuthenticateOidcActionConfig
from .el_bv2_fixed_response_action_config import ELBv2FixedResponseActionConfig
from .el_bv2_forward_action_config import ELBv2ForwardActionConfig
from .el_bv2_jwt_validation_action_config import ELBv2JwtValidationActionConfig
from .el_bv2_redirect_action_config import ELBv2RedirectActionConfig


class ELBv2Action(BaseModel):
    Type: StrictStr | None = None
    TargetGroupArn: StrictStr | None = None
    AuthenticateOidcConfig: ELBv2AuthenticateOidcActionConfig | None = None
    AuthenticateCognitoConfig: ELBv2AuthenticateCognitoActionConfig | None = None
    Order: StrictInt | None = None
    RedirectConfig: ELBv2RedirectActionConfig | None = None
    FixedResponseConfig: ELBv2FixedResponseActionConfig | None = None
    ForwardConfig: ELBv2ForwardActionConfig | None = None
    JwtValidationConfig: ELBv2JwtValidationActionConfig | None = None
