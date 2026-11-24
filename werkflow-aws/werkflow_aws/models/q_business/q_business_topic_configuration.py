from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_rule import QBusinessRule


class QBusinessTopicConfiguration(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    exampleChatMessages: list[StrictStr] | None = None
    rules: list[QBusinessRule] | None = None
