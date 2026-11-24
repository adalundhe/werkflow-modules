from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_optimization_config import SageMakerOptimizationConfig
from .sage_maker_optimization_job_model_source import SageMakerOptimizationJobModelSource
from .sage_maker_optimization_job_output_config import SageMakerOptimizationJobOutputConfig
from .sage_maker_optimization_vpc_config import SageMakerOptimizationVpcConfig
from .sage_maker_stopping_condition_model import SageMakerStoppingConditionModel
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateOptimizationJobRequest(BaseModel):
    OptimizationJobName: StrictStr
    RoleArn: StrictStr
    ModelSource: SageMakerOptimizationJobModelSource
    DeploymentInstanceType: StrictStr
    OptimizationConfigs: list[SageMakerOptimizationConfig]
    OutputConfig: SageMakerOptimizationJobOutputConfig
    StoppingCondition: SageMakerStoppingConditionModel
    MaxInstanceCount: StrictInt | None = None
    OptimizationEnvironment: dict[StrictStr, StrictStr] | None = None
    Tags: list[SageMakerTagModel] | None = None
    VpcConfig: SageMakerOptimizationVpcConfig | None = None
    TrainingPlanArns: list[StrictStr] | None = None
