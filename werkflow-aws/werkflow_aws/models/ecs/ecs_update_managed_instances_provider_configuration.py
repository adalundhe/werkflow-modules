from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecs_auto_repair_configuration import ECSAutoRepairConfiguration
from .ecs_infrastructure_optimization import ECSInfrastructureOptimization
from .ecs_instance_launch_template_update import ECSInstanceLaunchTemplateUpdate


class ECSUpdateManagedInstancesProviderConfiguration(BaseModel):
    infrastructureRoleArn: StrictStr
    instanceLaunchTemplate: ECSInstanceLaunchTemplateUpdate
    propagateTags: Literal['CAPACITY_PROVIDER', 'NONE'] | None = None
    infrastructureOptimization: ECSInfrastructureOptimization | None = None
    autoRepairConfiguration: ECSAutoRepairConfiguration | None = None
