from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .kinesis_analytics_code_content import KinesisAnalyticsCodeContent


class KinesisAnalyticsApplicationCodeConfiguration(BaseModel):
    CodeContentType: Literal['PLAINTEXT', 'ZIPFILE']
    CodeContent: KinesisAnalyticsCodeContent | None = None
