from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_code_content_description import KinesisAnalyticsCodeContentDescription


class KinesisAnalyticsApplicationCodeConfigurationDescription(BaseModel):
    CodeContentType: StrictStr | None = None
    CodeContentDescription: KinesisAnalyticsCodeContentDescription | None = None
