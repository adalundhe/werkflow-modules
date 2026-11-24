from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_infrastructure_optimization import BatchInfrastructureOptimization
from .batch_instance_launch_template import BatchInstanceLaunchTemplate


class BatchManagedInstancesProvider(BaseModel):
    propagateTags: StrictStr | None = None
    infrastructureRoleArn: StrictStr | None = None
    instanceLaunchTemplate: BatchInstanceLaunchTemplate | None = None
    infrastructureOptimization: BatchInfrastructureOptimization | None = None
