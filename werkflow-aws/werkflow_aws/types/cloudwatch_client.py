import datetime
from abc import ABC, abstractmethod
from typing import Literal, Any

CloudWatchMetricDimension = dict[
    Literal['Name', 'Value'],
    str
]

CloudWatchStatistics = Literal[
    "SampleCount",
    "Average",
    "Sum",
    "Minimum",
    "Maximum"
]


CloudWatchUnit = Literal[
    "Seconds",
    "Microseconds",
    "Milliseconds",
    "Bytes",
    'Kilobytes',
    'Megabytes',
    'Gigabytes',
    'Terabytes',
    'Bits',
    'Kilobits',
    'Megabits',
    'Gigabits',
    'Terabits',
    'Percent',
    'Count',
    'Bytes/Second',
    'Kilobytes/Second',
    'Megabytes/Second',
    'Gigabytes/Second',
    'Terabytes/Second',
    'Bits/Second',
    'Kilobits/Second',
    'Megabits/Second',
    'Gigabits/Second',
    'Terabits/Second',
    'Count/Second',
    'None'
]

CloudWatchScanBy = Literal[
    "TimestampDescending",
    "TimestampAscending",
]

CloudWatchLabelOptions = dict[
    Literal["Timezone"],
    str,
]

CloudWatchMetic = dict[
    Literal[
        "Namespace",
        "MetricName",
        "Dimensions"
    ],
    str | CloudWatchMetricDimension
]

CloudWatchMetricStat = dict[
    Literal[
        "Metric",
        "Period",
        "Stat",
        "Unit"
    ],
    str | int | CloudWatchMetic | CloudWatchUnit
]

CloudWatchMetricDataQuery = dict[
    Literal[
        "Id",
        "MetricStat",
        "Expression",
        "Label",
        "ReturnData",
        "Period",
        "AccountId",
    ],
    str | bool | int | CloudWatchMetricStat
]

class CloudWatchClient(ABC):

    @abstractmethod
    def get_metric_statistics(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: list[CloudWatchMetricDimension] | None = None,
        StartTime: datetime.datetime | None = None,
        EndTime: datetime.datetime | None = None,
        Period: int | None = None,
        Statistics: list[CloudWatchStatistics] | None = None,
        ExtendedStatistics: list[str] | None = None,
        Unit: CloudWatchUnit = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metrics(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: list[CloudWatchMetricDimension] | None = None,
        NextToken: str | None = None,
        RecentlyActive: Literal['PT3H'] = None,
        IncludeLinkedAccounts: bool = False,
        OwningAccount: str = None
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metric_data(
        self,
        MetricDataQueries: list[CloudWatchMetricDataQuery] = None,
        StartTime: datetime.datetime = None,
        EndTime: datetime.datetime = None,
        NextToken: str | None = None,
        ScanBy: CloudWatchScanBy =None,
        MaxDatapoints: int = None,
        LabelOptions: CloudWatchLabelOptions | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def close(self):
        pass