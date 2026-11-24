from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_oidc_config import SageMakerOidcConfig
from .sage_maker_source_ip_config import SageMakerSourceIpConfig
from .sage_maker_workforce_vpc_config_request import SageMakerWorkforceVpcConfigRequest


class SageMakerUpdateWorkforceRequest(BaseModel):
    WorkforceName: StrictStr
    SourceIpConfig: SageMakerSourceIpConfig | None = None
    OidcConfig: SageMakerOidcConfig | None = None
    WorkforceVpcConfig: SageMakerWorkforceVpcConfigRequest | None = None
    IpAddressType: Literal['ipv4', 'dualstack'] | None = None
