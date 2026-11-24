from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_parallelism_configuration_model import SageMakerParallelismConfigurationModel
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerPipeline(BaseModel):
    PipelineArn: StrictStr | None = None
    PipelineName: StrictStr | None = None
    PipelineDisplayName: StrictStr | None = None
    PipelineDescription: StrictStr | None = None
    RoleArn: StrictStr | None = None
    PipelineStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastRunTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    ParallelismConfiguration: SageMakerParallelismConfigurationModel | None = None
    Tags: list[SageMakerTagModel] | None = None
