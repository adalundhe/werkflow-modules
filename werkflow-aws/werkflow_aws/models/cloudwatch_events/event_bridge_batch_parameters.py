from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_batch_array_properties import EventBridgeBatchArrayProperties
from .event_bridge_batch_retry_strategy import EventBridgeBatchRetryStrategy


class EventBridgeBatchParameters(BaseModel):
    JobDefinition: StrictStr | None = None
    JobName: StrictStr | None = None
    ArrayProperties: EventBridgeBatchArrayProperties | None = None
    RetryStrategy: EventBridgeBatchRetryStrategy | None = None
