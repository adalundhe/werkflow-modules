from __future__ import annotations
from pydantic import BaseModel
from .q_business_content_blocker_rule import QBusinessContentBlockerRule
from .q_business_content_retrieval_rule import QBusinessContentRetrievalRule


class QBusinessRuleConfiguration(BaseModel):
    contentBlockerRule: QBusinessContentBlockerRule | None = None
    contentRetrievalRule: QBusinessContentRetrievalRule | None = None
