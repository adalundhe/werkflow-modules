from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_parallelism_configuration import SageMakerParallelismConfiguration
from .sage_maker_parameter import SageMakerParameter
from .sage_maker_selective_execution_config import SageMakerSelectiveExecutionConfig


class SageMakerStartPipelineExecutionRequest(BaseModel):
    PipelineName: StrictStr
    PipelineExecutionDisplayName: StrictStr | None = None
    PipelineParameters: list[SageMakerParameter] | None = None
    PipelineExecutionDescription: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    ParallelismConfiguration: SageMakerParallelismConfiguration | None = None
    SelectiveExecutionConfig: SageMakerSelectiveExecutionConfig | None = None
    PipelineVersionId: StrictInt | None = None
    MlflowExperimentName: StrictStr | None = None
    PipelineVersionAlias: StrictStr | None = None
    RoleArn: StrictStr | None = None
