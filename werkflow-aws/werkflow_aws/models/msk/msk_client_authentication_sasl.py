from pydantic import BaseModel
from .msk_client_authentication_sasl_iam import MSKClientAuthenticationSaslIAm
from .msk_client_authentication_sasl_scram import MSKClientAuthenticationSaslScram

class MSKClientAuthenticationSasl(BaseModel):
    Scram: MSKClientAuthenticationSaslScram
    Iam: MSKClientAuthenticationSaslIAm