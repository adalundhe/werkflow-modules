from __future__ import annotations
from pydantic import BaseModel, StrictStr
from typing import Literal
from .dump_options import DumpOptions
from .expression import Expression
from .group import Group
from .time_period import TimePeriod


ValidMetrics = Literal[
    "AmortizedCost",
    "BlendedCost",
    "NetAmortizedCost",
    "NetUnblendedCost",
    "NormalizedUsageAmount",
    "UnblendedCost",
    "UsageQuantity",
]



class CostExplorerQuery(BaseModel):
    TimePeriod: TimePeriod
    Granularity: Literal['DAILY', 'MONTHLY', 'HOURLY'] = 'MONTHLY'
    Filter: Expression | None = None
    Metrics: list[ValidMetrics]
    GroupBy: list[Group] | None = None
    BillingViewArn: StrictStr | None = None
    NextPageToken: StrictStr | None = None

    def dump(self, options: DumpOptions | None = None):
        if options is None:
            options = DumpOptions(
                time_format='%Y-%m',
            )

        return {
            'TimePeriod': self.TimePeriod.dump(options.time_format),
            'Granularity': self.Granularity,
            'Filter': self.Filter.dump(),
            'Metrics': self.Metrics,
            'GroupBy': [
                group.dump() for group in self.GroupBy
            ]
        }