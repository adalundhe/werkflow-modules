from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_m_lflow_configuration import SageMakerMLflowConfiguration
from .sage_maker_parallelism_configuration_model import SageMakerParallelismConfigurationModel
from .sage_maker_pipeline_experiment_config import SageMakerPipelineExperimentConfig
from .sage_maker_selective_execution_config_model import SageMakerSelectiveExecutionConfigModel
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribePipelineExecutionResponse(BaseModel):
    PipelineArn: StrictStr | None = None
    PipelineExecutionArn: StrictStr | None = None
    PipelineExecutionDisplayName: StrictStr | None = None
    PipelineExecutionStatus: StrictStr | None = None
    PipelineExecutionDescription: StrictStr | None = None
    PipelineExperimentConfig: SageMakerPipelineExperimentConfig | None = None
    FailureReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    ParallelismConfiguration: SageMakerParallelismConfigurationModel | None = None
    SelectiveExecutionConfig: SageMakerSelectiveExecutionConfigModel | None = None
    PipelineVersionId: StrictInt | None = None
    MLflowConfig: SageMakerMLflowConfiguration | None = None
    PipelineVersionAliases: list[StrictStr] | None = None
    RoleArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
