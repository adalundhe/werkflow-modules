from pydantic import BaseModel
from .msk_client_authentication_sasl import MSKClientAuthenticationSasl
from .msk_vpc_client_authentication_tls import MSKVPCClientAuthenticationTls


class MSKVPCClientAuthentication(BaseModel):
    Sasl: MSKClientAuthenticationSasl
    Tls: MSKVPCClientAuthenticationTls

