from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_reference import QuickSightDataSetReference
from .quick_sight_topic_reference import QuickSightTopicReference


class QuickSightTemplateSourceAnalysis(BaseModel):
    Arn: StrictStr
    DataSetReferences: list[QuickSightDataSetReference]
    TopicReferences: list[QuickSightTopicReference] | None = None
