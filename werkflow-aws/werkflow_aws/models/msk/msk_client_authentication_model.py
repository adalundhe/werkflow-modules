from __future__ import annotations
from pydantic import BaseModel
from .msk_sasl import MSKSasl
from .msk_tls import MSKTls
from .msk_unauthenticated import MSKUnauthenticated


class MSKClientAuthenticationModel(BaseModel):
    Sasl: MSKSasl | None = None
    Tls: MSKTls | None = None
    Unauthenticated: MSKUnauthenticated | None = None
