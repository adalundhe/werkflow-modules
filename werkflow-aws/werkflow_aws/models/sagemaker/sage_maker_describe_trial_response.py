from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_trial_source import SageMakerTrialSource
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeTrialResponse(BaseModel):
    TrialName: StrictStr | None = None
    TrialArn: StrictStr | None = None
    DisplayName: StrictStr | None = None
    ExperimentName: StrictStr | None = None
    Source: SageMakerTrialSource | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
