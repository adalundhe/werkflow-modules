from pydantic import BaseModel, StrictBool


class MSKVPCClientAuthenticationTls(BaseModel):
    Enabled: StrictBool = False
    