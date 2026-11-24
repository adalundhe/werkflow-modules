from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_cipher import ELBv2Cipher


class ELBv2SslPolicy(BaseModel):
    SslProtocols: list[StrictStr] | None = None
    Ciphers: list[ELBv2Cipher] | None = None
    Name: StrictStr | None = None
    SupportedLoadBalancerTypes: list[StrictStr] | None = None
