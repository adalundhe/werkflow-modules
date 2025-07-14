from pydantic import BaseModel, StrictBool


class MSKClientAuthenticationSaslIAm(BaseModel):
    Enabled: StrictBool = False
    