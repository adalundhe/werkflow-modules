from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_conditional_rule import EndUserMessagingConditionalRule


class EndUserMessagingConditionalBehavior(BaseModel):
    Rules: list[EndUserMessagingConditionalRule] | None = None
    DefaultBehavior: StrictStr | None = None
