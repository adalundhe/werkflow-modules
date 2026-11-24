from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsIntentGroupBySpecification(BaseModel):
    name: Literal['IntentName', 'IntentEndState', 'IntentLevel']
