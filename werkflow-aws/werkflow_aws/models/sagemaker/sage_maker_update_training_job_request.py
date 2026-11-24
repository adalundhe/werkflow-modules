from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_profiler_config_for_update import SageMakerProfilerConfigForUpdate
from .sage_maker_profiler_rule_configuration_model import SageMakerProfilerRuleConfigurationModel
from .sage_maker_remote_debug_config_for_update import SageMakerRemoteDebugConfigForUpdate
from .sage_maker_resource_config_for_update import SageMakerResourceConfigForUpdate


class SageMakerUpdateTrainingJobRequest(BaseModel):
    TrainingJobName: StrictStr
    ProfilerConfig: SageMakerProfilerConfigForUpdate | None = None
    ProfilerRuleConfigurations: list[SageMakerProfilerRuleConfigurationModel] | None = None
    ResourceConfig: SageMakerResourceConfigForUpdate | None = None
    RemoteDebugConfig: SageMakerRemoteDebugConfigForUpdate | None = None
