from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_cognito_config import SageMakerCognitoConfig
from .sage_maker_oidc_config_for_response import SageMakerOidcConfigForResponse
from .sage_maker_source_ip_config import SageMakerSourceIpConfig
from .sage_maker_workforce_vpc_config_response import SageMakerWorkforceVpcConfigResponse


class SageMakerWorkforce(BaseModel):
    WorkforceName: StrictStr | None = None
    WorkforceArn: StrictStr | None = None
    LastUpdatedDate: datetime.datetime | StrictStr | None = None
    SourceIpConfig: SageMakerSourceIpConfig | None = None
    SubDomain: StrictStr | None = None
    CognitoConfig: SageMakerCognitoConfig | None = None
    OidcConfig: SageMakerOidcConfigForResponse | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    WorkforceVpcConfig: SageMakerWorkforceVpcConfigResponse | None = None
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
    IpAddressType: StrictStr | None = None
