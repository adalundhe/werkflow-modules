from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_cognito_config import SageMakerCognitoConfig
from .sage_maker_oidc_config import SageMakerOidcConfig
from .sage_maker_source_ip_config import SageMakerSourceIpConfig
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_workforce_vpc_config_request import SageMakerWorkforceVpcConfigRequest


class SageMakerCreateWorkforceRequest(BaseModel):
    WorkforceName: StrictStr
    CognitoConfig: SageMakerCognitoConfig | None = None
    OidcConfig: SageMakerOidcConfig | None = None
    SourceIpConfig: SageMakerSourceIpConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
    WorkforceVpcConfig: SageMakerWorkforceVpcConfigRequest | None = None
    IpAddressType: Literal['ipv4', 'dualstack'] | None = None
