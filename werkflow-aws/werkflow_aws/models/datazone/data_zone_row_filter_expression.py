from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .data_zone_equal_to_expression import DataZoneEqualToExpression
from .data_zone_greater_than_expression import DataZoneGreaterThanExpression
from .data_zone_greater_than_or_equal_to_expression import DataZoneGreaterThanOrEqualToExpression
from .data_zone_in_expression import DataZoneInExpression
from .data_zone_is_not_null_expression import DataZoneIsNotNullExpression
from .data_zone_is_null_expression import DataZoneIsNullExpression
from .data_zone_less_than_expression import DataZoneLessThanExpression
from .data_zone_less_than_or_equal_to_expression import DataZoneLessThanOrEqualToExpression
from .data_zone_like_expression import DataZoneLikeExpression
from .data_zone_not_equal_to_expression import DataZoneNotEqualToExpression
from .data_zone_not_in_expression import DataZoneNotInExpression
from .data_zone_not_like_expression import DataZoneNotLikeExpression


class DataZoneRowFilterExpression(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    equalTo: DataZoneEqualToExpression | None = None
    notEqualTo: DataZoneNotEqualToExpression | None = None
    greaterThan: DataZoneGreaterThanExpression | None = None
    lessThan: DataZoneLessThanExpression | None = None
    greaterThanOrEqualTo: DataZoneGreaterThanOrEqualToExpression | None = None
    lessThanOrEqualTo: DataZoneLessThanOrEqualToExpression | None = None
    isNull: DataZoneIsNullExpression | None = None
    isNotNull: DataZoneIsNotNullExpression | None = None
    in_: DataZoneInExpression | None = Field(default=None, alias='in')
    notIn: DataZoneNotInExpression | None = None
    like: DataZoneLikeExpression | None = None
    notLike: DataZoneNotLikeExpression | None = None
