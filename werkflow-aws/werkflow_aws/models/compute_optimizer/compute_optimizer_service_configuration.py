from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_container_configuration import ComputeOptimizerContainerConfiguration


class ComputeOptimizerServiceConfiguration(BaseModel):
    memory: StrictInt | None = None
    cpu: StrictInt | None = None
    containerConfigurations: list[ComputeOptimizerContainerConfiguration] | None = None
    autoScalingConfiguration: StrictStr | None = None
    taskDefinitionArn: StrictStr | None = None
