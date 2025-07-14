from pydantic import BaseModel, StrictInt, StrictBool


class MSKEBSPRovisionedThroughtput(BaseModel):
    Enabled: StrictBool = False
    VolumeSize: StrictInt = 0