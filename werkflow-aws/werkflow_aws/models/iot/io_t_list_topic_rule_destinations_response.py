from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_topic_rule_destination_summary import IoTTopicRuleDestinationSummary


class IoTListTopicRuleDestinationsResponse(BaseModel):
    destinationSummaries: list[IoTTopicRuleDestinationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
