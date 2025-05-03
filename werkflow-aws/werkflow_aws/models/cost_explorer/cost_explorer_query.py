from __future__ import annotations
from pydantic import BaseModel, StrictStr
from typing import Literal
from .dump_options import DumpOptions
from .expression import Expression
from .group import Group
from .granularity import AWSGranularityLevel
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
    Granularity: AWSGranularityLevel = 'MONTHLY'
    Filter: Expression | None = None
    Metrics: list[ValidMetrics]
    GroupBy: list[Group] | None = None
    BillingViewArn: StrictStr | None = None
    NextPageToken: StrictStr | None = None

    def dump(self, options: DumpOptions | None = None):
        if options is None:
            options = DumpOptions(
                time_format='%Y-%m-%d',
            )

        dumped = {
            'TimePeriod': self.TimePeriod.dump(options.time_format),
            'Granularity': self.Granularity,
            'Metrics': self.Metrics,
        }

        if filters := self.Filter:
            dumped['Filter'] = filters.dump()

        if groups := self.GroupBy:
            dumped['GroupBy'] = [
                group.dump() for group in groups
            ]

        if self.BillingViewArn:
            dumped['BillingViewArn'] = self.BillingViewArn

        if self.NextPageToken:
            dumped['NextPageToken'] = self.NextPageToken

        return dumped