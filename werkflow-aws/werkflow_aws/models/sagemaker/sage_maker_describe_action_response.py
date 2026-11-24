from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_action_source import SageMakerActionSource
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeActionResponse(BaseModel):
    ActionName: StrictStr | None = None
    ActionArn: StrictStr | None = None
    Source: SageMakerActionSource | None = None
    ActionType: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    LineageGroupArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
