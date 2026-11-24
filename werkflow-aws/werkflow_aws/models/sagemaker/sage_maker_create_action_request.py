from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_action_source import SageMakerActionSource
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateActionRequest(BaseModel):
    ActionName: StrictStr
    Source: SageMakerActionSource
    ActionType: StrictStr
    Description: StrictStr | None = None
    Status: Literal['Unknown', 'InProgress', 'Completed', 'Failed', 'Stopping', 'Stopped'] | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    Tags: list[SageMakerTagModel] | None = None
