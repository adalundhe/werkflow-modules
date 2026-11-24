from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EKSConnectorConfigRequest(BaseModel):
    roleArn: StrictStr
    provider: Literal['EKS_ANYWHERE', 'ANTHOS', 'GKE', 'AKS', 'OPENSHIFT', 'TANZU', 'RANCHER', 'EC2', 'OTHER']
