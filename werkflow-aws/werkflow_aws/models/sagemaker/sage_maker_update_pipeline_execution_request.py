from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_parallelism_configuration_model import SageMakerParallelismConfigurationModel


class SageMakerUpdatePipelineExecutionRequest(BaseModel):
    PipelineExecutionArn: StrictStr
    PipelineExecutionDescription: StrictStr | None = None
    PipelineExecutionDisplayName: StrictStr | None = None
    ParallelismConfiguration: SageMakerParallelismConfigurationModel | None = None
