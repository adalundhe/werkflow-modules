from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_infrastructure_optimization import BatchInfrastructureOptimization
from .batch_instance_launch_template_update import BatchInstanceLaunchTemplateUpdate


class BatchUpdateManagedInstancesProviderConfiguration(BaseModel):
    propagateTags: StrictStr | None = None
    infrastructureRoleArn: StrictStr | None = None
    instanceLaunchTemplate: BatchInstanceLaunchTemplateUpdate | None = None
    infrastructureOptimization: BatchInfrastructureOptimization | None = None
