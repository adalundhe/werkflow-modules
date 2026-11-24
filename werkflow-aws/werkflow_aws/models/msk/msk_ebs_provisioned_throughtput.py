from pydantic import BaseModel, StrictBool, StrictInt


class MSKEBSProvisionedThroughput(BaseModel):
    Enabled: StrictBool | None = None
    VolumeThroughput: StrictInt | None = None


MSKEBSPRovisionedThroughtput = MSKEBSProvisionedThroughput
