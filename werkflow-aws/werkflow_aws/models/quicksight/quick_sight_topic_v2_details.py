from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_topic_v2_data_set_reference import QuickSightTopicV2DataSetReference
from .quick_sight_topic_v2_data_set_relation import QuickSightTopicV2DataSetRelation


class QuickSightTopicV2Details(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    DataSets: list[QuickSightTopicV2DataSetReference] | None = None
    DataSetRelations: list[QuickSightTopicV2DataSetRelation] | None = None
