from __future__ import annotations
from pydantic import BaseModel
from .ses_batch_get_metric_data_query import SESBatchGetMetricDataQuery


class SESBatchGetMetricDataRequest(BaseModel):
    Queries: list[SESBatchGetMetricDataQuery]
