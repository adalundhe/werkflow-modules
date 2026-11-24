from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .el_bv2_action import ELBv2Action
from .el_bv2_certificate import ELBv2Certificate
from .el_bv2_mutual_authentication_attributes import ELBv2MutualAuthenticationAttributes


class ELBv2Listener(BaseModel):
    ListenerArn: StrictStr | None = None
    LoadBalancerArn: StrictStr | None = None
    Port: StrictInt | None = None
    Protocol: StrictStr | None = None
    Certificates: list[ELBv2Certificate] | None = None
    SslPolicy: StrictStr | None = None
    DefaultActions: list[ELBv2Action] | None = None
    AlpnPolicy: list[StrictStr] | None = None
    MutualAuthentication: ELBv2MutualAuthenticationAttributes | None = None
