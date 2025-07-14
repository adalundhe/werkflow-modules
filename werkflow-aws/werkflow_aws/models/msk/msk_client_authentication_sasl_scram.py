from pydantic import BaseModel, StrictBool


class MSKClientAuthenticationSaslScram(BaseModel):
    Enabled: StrictBool = False
    