from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .el_bv2_action import ELBv2Action
from .el_bv2_certificate import ELBv2Certificate
from .el_bv2_mutual_authentication_attributes import ELBv2MutualAuthenticationAttributes
from .el_bv2_tag import ELBv2Tag


class ELBv2CreateListenerRequest(BaseModel):
    LoadBalancerArn: StrictStr
    DefaultActions: list[ELBv2Action]
    Protocol: Literal['HTTP', 'HTTPS', 'TCP', 'TLS', 'UDP', 'TCP_UDP', 'GENEVE', 'QUIC', 'TCP_QUIC'] | None = None
    Port: StrictInt | None = None
    SslPolicy: StrictStr | None = None
    Certificates: list[ELBv2Certificate] | None = None
    AlpnPolicy: list[StrictStr] | None = None
    Tags: list[ELBv2Tag] | None = None
    MutualAuthentication: ELBv2MutualAuthenticationAttributes | None = None
