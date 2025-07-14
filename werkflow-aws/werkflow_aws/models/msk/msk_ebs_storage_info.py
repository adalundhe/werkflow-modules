from pydantic import BaseModel, StrictInt
from .msk_ebs_provisioned_throughtput import MSKEBSPRovisionedThroughtput


class MSKEBSStorageInfo(BaseModel):
    ProvisionedThroughput: MSKEBSPRovisionedThroughtput
    VolumeSize: StrictInt