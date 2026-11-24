from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_topic_v2_data_set_relation_endpoint import QuickSightTopicV2DataSetRelationEndpoint


class QuickSightTopicV2DataSetRelation(BaseModel):
    Left: QuickSightTopicV2DataSetRelationEndpoint | None = None
    Right: QuickSightTopicV2DataSetRelationEndpoint | None = None
