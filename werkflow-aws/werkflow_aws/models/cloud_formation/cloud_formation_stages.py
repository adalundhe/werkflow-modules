from __future__ import annotations
from pydantic import BaseModel
from .cloud_formation_role_provisioning import CloudFormationRoleProvisioning
from .cloud_formation_stack_instances_deployment import CloudFormationStackInstancesDeployment


class CloudFormationStages(BaseModel):
    RoleProvisioning: CloudFormationRoleProvisioning | None = None
    StackInstancesDeployment: CloudFormationStackInstancesDeployment | None = None
