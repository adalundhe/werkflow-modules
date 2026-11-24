from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_parallelism_configuration_model import SageMakerParallelismConfigurationModel


class SageMakerRetryPipelineExecutionRequest(BaseModel):
    PipelineExecutionArn: StrictStr
    ClientRequestToken: StrictStr
    ParallelismConfiguration: SageMakerParallelismConfigurationModel | None = None
