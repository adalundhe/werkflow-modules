from __future__ import annotations
from pydantic import BaseModel
from .cloud_formation_regional_stack_instances_deployment import CloudFormationRegionalStackInstancesDeployment


class CloudFormationRegionalStages(BaseModel):
    RegionalStackInstancesDeployment: CloudFormationRegionalStackInstancesDeployment | None = None
