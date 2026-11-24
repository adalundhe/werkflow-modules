from pydantic import BaseModel, StrictInt
from .msk_ebs_provisioned_throughtput import MSKEBSProvisionedThroughput


class MSKEBSStorageInfo(BaseModel):
    ProvisionedThroughput: MSKEBSProvisionedThroughput | None = None
    VolumeSize: StrictInt | None = None
