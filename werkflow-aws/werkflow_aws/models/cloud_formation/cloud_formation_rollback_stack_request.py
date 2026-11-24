from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_deployment_config import CloudFormationDeploymentConfig


class CloudFormationRollbackStackRequest(BaseModel):
    StackName: StrictStr
    RoleARN: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    RetainExceptOnCreate: StrictBool | None = None
    DeploymentConfig: CloudFormationDeploymentConfig | None = None
