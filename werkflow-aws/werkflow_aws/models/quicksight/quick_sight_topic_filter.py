from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_topic_category_filter import QuickSightTopicCategoryFilter
from .quick_sight_topic_date_range_filter import QuickSightTopicDateRangeFilter
from .quick_sight_topic_null_filter import QuickSightTopicNullFilter
from .quick_sight_topic_numeric_equality_filter import QuickSightTopicNumericEqualityFilter
from .quick_sight_topic_numeric_range_filter import QuickSightTopicNumericRangeFilter
from .quick_sight_topic_relative_date_filter import QuickSightTopicRelativeDateFilter


class QuickSightTopicFilter(BaseModel):
    FilterDescription: StrictStr | None = None
    FilterClass: StrictStr | None = None
    FilterName: StrictStr | None = None
    FilterSynonyms: list[StrictStr] | None = None
    OperandFieldName: StrictStr | None = None
    FilterType: StrictStr | None = None
    CategoryFilter: QuickSightTopicCategoryFilter | None = None
    NumericEqualityFilter: QuickSightTopicNumericEqualityFilter | None = None
    NumericRangeFilter: QuickSightTopicNumericRangeFilter | None = None
    DateRangeFilter: QuickSightTopicDateRangeFilter | None = None
    RelativeDateFilter: QuickSightTopicRelativeDateFilter | None = None
    NullFilter: QuickSightTopicNullFilter | None = None
