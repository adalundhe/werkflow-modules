from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_parallelism_configuration import SageMakerParallelismConfiguration
from .sage_maker_pipeline_status import SageMakerPipelineStatus
from .sage_maker_user_context import SageMakerUserContext


class SageMakerDescribePipelineResponse(BaseModel):
    PipelineArn: StrictStr | None = None
    PipelineName: StrictStr | None = None
    PipelineDisplayName: StrictStr | None = None
    PipelineDefinition: StrictStr | None = None
    PipelineDescription: StrictStr | None = None
    RoleArn: StrictStr | None = None
    PipelineStatus: SageMakerPipelineStatus | None = None
    CreationTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    LastRunTime: datetime.datetime | None = None
    CreatedBy: SageMakerUserContext | None = None
    LastModifiedBy: SageMakerUserContext | None = None
    ParallelismConfiguration: SageMakerParallelismConfiguration | None = None
    PipelineVersionDisplayName: StrictStr | None = None
    PipelineVersionDescription: StrictStr | None = None
    PipelineVersionAliases: list[StrictStr] | None = None
