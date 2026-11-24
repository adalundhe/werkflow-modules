from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dataset_metadata import QuickSightDatasetMetadata
from .quick_sight_topic_config_options import QuickSightTopicConfigOptions


class QuickSightTopicDetails(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    UserExperienceVersion: StrictStr | None = None
    DataSets: list[QuickSightDatasetMetadata] | None = None
    ConfigOptions: QuickSightTopicConfigOptions | None = None
