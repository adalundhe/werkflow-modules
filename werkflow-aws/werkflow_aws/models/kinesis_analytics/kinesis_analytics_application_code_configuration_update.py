from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .kinesis_analytics_code_content_update import KinesisAnalyticsCodeContentUpdate


class KinesisAnalyticsApplicationCodeConfigurationUpdate(BaseModel):
    CodeContentTypeUpdate: Literal['PLAINTEXT', 'ZIPFILE'] | None = None
    CodeContentUpdate: KinesisAnalyticsCodeContentUpdate | None = None
