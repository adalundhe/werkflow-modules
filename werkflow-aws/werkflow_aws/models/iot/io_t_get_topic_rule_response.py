from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_topic_rule import IoTTopicRule


class IoTGetTopicRuleResponse(BaseModel):
    ruleArn: StrictStr | None = None
    rule: IoTTopicRule | None = None
    ResponseMetadata: dict[str, Any] | None = None
