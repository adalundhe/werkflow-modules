from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_aggregation import QuickSightDataAggregation
from .quick_sight_topic_calculated_field import QuickSightTopicCalculatedField
from .quick_sight_topic_column import QuickSightTopicColumn
from .quick_sight_topic_filter import QuickSightTopicFilter
from .quick_sight_topic_named_entity import QuickSightTopicNamedEntity


class QuickSightDatasetMetadata(BaseModel):
    DatasetArn: StrictStr | None = None
    DatasetName: StrictStr | None = None
    DatasetDescription: StrictStr | None = None
    DataAggregation: QuickSightDataAggregation | None = None
    Filters: list[QuickSightTopicFilter] | None = None
    Columns: list[QuickSightTopicColumn] | None = None
    CalculatedFields: list[QuickSightTopicCalculatedField] | None = None
    NamedEntities: list[QuickSightTopicNamedEntity] | None = None
