from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ses_topic_filter import SESTopicFilter


class SESListContactsFilter(BaseModel):
    FilteredStatus: Literal['OPT_IN', 'OPT_OUT'] | None = None
    TopicFilter: SESTopicFilter | None = None
