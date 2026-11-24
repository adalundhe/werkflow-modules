from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KendraGetSnapshotsRequest(BaseModel):
    IndexId: StrictStr
    Interval: Literal['THIS_MONTH', 'THIS_WEEK', 'ONE_WEEK_AGO', 'TWO_WEEKS_AGO', 'ONE_MONTH_AGO', 'TWO_MONTHS_AGO']
    MetricType: Literal['QUERIES_BY_COUNT', 'QUERIES_BY_ZERO_CLICK_RATE', 'QUERIES_BY_ZERO_RESULT_RATE', 'DOCS_BY_CLICK_COUNT', 'AGG_QUERY_DOC_METRICS', 'TREND_QUERY_DOC_METRICS']
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
