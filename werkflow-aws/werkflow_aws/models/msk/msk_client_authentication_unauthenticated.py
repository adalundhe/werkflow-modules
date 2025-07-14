from pydantic import BaseModel, StrictBool


class MSKClientAuthenticationUnauthenticated(BaseModel):
    Enabled: StrictBool = False
    