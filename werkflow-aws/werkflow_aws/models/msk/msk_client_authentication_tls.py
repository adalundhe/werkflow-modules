from pydantic import BaseModel, StrictStr, StrictBool


class MSKClientAuthenticationTls(BaseModel):
    CertificateAuthorityArnList: list[StrictStr]
    Enabled: StrictBool = False