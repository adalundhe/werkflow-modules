from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IoTTopicRuleListItem(BaseModel):
    ruleArn: StrictStr | None = None
    ruleName: StrictStr | None = None
    topicPattern: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    ruleDisabled: StrictBool | None = None
