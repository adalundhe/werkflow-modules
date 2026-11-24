from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSAddonPodIdentityAssociations(BaseModel):
    serviceAccount: StrictStr
    roleArn: StrictStr
