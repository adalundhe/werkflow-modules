from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_topic_rule_payload import IoTTopicRulePayload


class IoTCreateTopicRuleRequest(BaseModel):
    ruleName: StrictStr
    topicRulePayload: IoTTopicRulePayload
    tags: StrictStr | None = None
