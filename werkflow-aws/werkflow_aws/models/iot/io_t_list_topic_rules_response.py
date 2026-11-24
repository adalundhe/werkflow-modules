from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_topic_rule_list_item import IoTTopicRuleListItem


class IoTListTopicRulesResponse(BaseModel):
    rules: list[IoTTopicRuleListItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
