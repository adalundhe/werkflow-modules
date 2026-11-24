from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_s3_application_code_location_description import KinesisAnalyticsS3ApplicationCodeLocationDescription


class KinesisAnalyticsCodeContentDescription(BaseModel):
    TextContent: StrictStr | None = None
    CodeMD5: StrictStr | None = None
    CodeSize: StrictInt | None = None
    S3ApplicationCodeLocationDescription: KinesisAnalyticsS3ApplicationCodeLocationDescription | None = None
