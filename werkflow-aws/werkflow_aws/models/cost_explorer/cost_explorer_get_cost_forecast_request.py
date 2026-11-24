from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .expression import Expression
from .granularity import AWSGranularityLevel
from .granularity import Granularity
from .metric import Metric
from .time_period import TimePeriod as CETimePeriod


class CostExplorerGetCostForecastRequest(BaseModel):
    TimePeriod: CETimePeriod
    Metric: StrictStr
    Granularity: AWSGranularityLevel
    Filter: Expression | None = None
    BillingViewArn: StrictStr | None = None
    PredictionIntervalLevel: StrictInt | None = None
