from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerPipelineVersion(BaseModel):
    PipelineArn: StrictStr | None = None
    PipelineVersionId: StrictInt | None = None
    PipelineVersionDisplayName: StrictStr | None = None
    PipelineVersionDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    LastExecutedPipelineExecutionArn: StrictStr | None = None
    LastExecutedPipelineExecutionDisplayName: StrictStr | None = None
    LastExecutedPipelineExecutionStatus: StrictStr | None = None
    PipelineVersionAliases: list[StrictStr] | None = None
