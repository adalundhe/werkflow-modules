from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_topic_rule_destination import IoTTopicRuleDestination


class IoTGetTopicRuleDestinationResponse(BaseModel):
    topicRuleDestination: IoTTopicRuleDestination | None = None
    ResponseMetadata: dict[str, Any] | None = None
