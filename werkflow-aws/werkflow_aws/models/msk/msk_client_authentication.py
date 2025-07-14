from pydantic import BaseModel
from .msk_client_authentication_sasl import MSKClientAuthenticationSasl
from .msk_client_authentication_tls import MSKClientAuthenticationTls
from .msk_client_authentication_unauthenticated import MSKClientAuthenticationUnauthenticated


class MSKClientAuthentication(BaseModel):
    Sasl: MSKClientAuthenticationSasl
    Tls: MSKClientAuthenticationTls
    Unauthenticated: MSKClientAuthenticationUnauthenticated
