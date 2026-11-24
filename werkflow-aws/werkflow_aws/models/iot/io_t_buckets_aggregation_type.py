from __future__ import annotations
from pydantic import BaseModel
from .io_t_terms_aggregation import IoTTermsAggregation


class IoTBucketsAggregationType(BaseModel):
    termsAggregation: IoTTermsAggregation | None = None
