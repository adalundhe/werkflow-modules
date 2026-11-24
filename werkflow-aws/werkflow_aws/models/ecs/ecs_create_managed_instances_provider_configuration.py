from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecs_auto_repair_configuration import ECSAutoRepairConfiguration
from .ecs_infrastructure_optimization import ECSInfrastructureOptimization
from .ecs_instance_launch_template import ECSInstanceLaunchTemplate


class ECSCreateManagedInstancesProviderConfiguration(BaseModel):
    infrastructureRoleArn: StrictStr
    instanceLaunchTemplate: ECSInstanceLaunchTemplate
    propagateTags: Literal['CAPACITY_PROVIDER', 'NONE'] | None = None
    infrastructureOptimization: ECSInfrastructureOptimization | None = None
    autoRepairConfiguration: ECSAutoRepairConfiguration | None = None
