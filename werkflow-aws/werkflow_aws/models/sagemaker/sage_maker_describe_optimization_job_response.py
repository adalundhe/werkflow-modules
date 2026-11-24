from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_optimization_config import SageMakerOptimizationConfig
from .sage_maker_optimization_job_model_source import SageMakerOptimizationJobModelSource
from .sage_maker_optimization_job_output_config import SageMakerOptimizationJobOutputConfig
from .sage_maker_optimization_output import SageMakerOptimizationOutput
from .sage_maker_optimization_vpc_config import SageMakerOptimizationVpcConfig
from .sage_maker_stopping_condition_model import SageMakerStoppingConditionModel


class SageMakerDescribeOptimizationJobResponse(BaseModel):
    OptimizationJobArn: StrictStr | None = None
    OptimizationJobStatus: StrictStr | None = None
    OptimizationStartTime: datetime.datetime | StrictStr | None = None
    OptimizationEndTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    OptimizationJobName: StrictStr | None = None
    ModelSource: SageMakerOptimizationJobModelSource | None = None
    OptimizationEnvironment: dict[StrictStr, StrictStr] | None = None
    DeploymentInstanceType: StrictStr | None = None
    MaxInstanceCount: StrictInt | None = None
    OptimizationConfigs: list[SageMakerOptimizationConfig] | None = None
    OutputConfig: SageMakerOptimizationJobOutputConfig | None = None
    OptimizationOutput: SageMakerOptimizationOutput | None = None
    RoleArn: StrictStr | None = None
    StoppingCondition: SageMakerStoppingConditionModel | None = None
    VpcConfig: SageMakerOptimizationVpcConfig | None = None
    TrainingPlanArns: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
