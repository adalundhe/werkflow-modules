from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .connect_available_filter import ConnectAvailableFilter
from .connect_created_by_info import ConnectCreatedByInfo
from .connect_metric_calculation import ConnectMetricCalculation


class ConnectMetricDefinition(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    MetricCalculation: ConnectMetricCalculation | None = None
    CreationMethod: StrictStr | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
    Unit: StrictStr | None = None
    PositiveTrendIndicator: StrictStr | None = None
    Groupings: list[StrictStr] | None = None
    Filters: list[ConnectAvailableFilter] | None = None
    EffectiveTime: datetime.datetime | StrictStr | None = None
    RefreshRate: StrictInt | None = None
    Category: StrictStr | None = None
    SupportedStats: list[StrictStr] | None = None
    DefaultStat: StrictStr | None = None
    SupportsPreaggregateCalculation: StrictBool | None = None
    SupportsCustomCalculation: StrictBool | None = None
    PrimaryEventSource: StrictStr | None = None
    PrimaryEventSourceEffectiveTimestampType: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedUser: ConnectCreatedByInfo | None = None
    LastModifiedRegion: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedUser: ConnectCreatedByInfo | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
