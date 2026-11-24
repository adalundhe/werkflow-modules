from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_experiment_source import SageMakerExperimentSource
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerExperiment(BaseModel):
    ExperimentName: StrictStr | None = None
    ExperimentArn: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Source: SageMakerExperimentSource | None = None
    Description: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    Tags: list[SageMakerTagModel] | None = None
