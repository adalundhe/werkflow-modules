from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_formation_deployment_config import CloudFormationDeploymentConfig


class CloudFormationDeleteStackRequest(BaseModel):
    StackName: StrictStr
    RetainResources: list[StrictStr] | None = None
    RoleARN: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    DeletionMode: Literal['STANDARD', 'FORCE_DELETE_STACK'] | None = None
    DeploymentConfig: CloudFormationDeploymentConfig | None = None
