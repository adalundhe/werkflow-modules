from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_auto_repair_configuration import ECSAutoRepairConfiguration
from .ecs_infrastructure_optimization import ECSInfrastructureOptimization
from .ecs_instance_launch_template import ECSInstanceLaunchTemplate


class ECSManagedInstancesProvider(BaseModel):
    infrastructureRoleArn: StrictStr | None = None
    instanceLaunchTemplate: ECSInstanceLaunchTemplate | None = None
    propagateTags: StrictStr | None = None
    infrastructureOptimization: ECSInfrastructureOptimization | None = None
    autoRepairConfiguration: ECSAutoRepairConfiguration | None = None
