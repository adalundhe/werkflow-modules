from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .kinesis_analytics_s3_content_location import KinesisAnalyticsS3ContentLocation


class KinesisAnalyticsCodeContent(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    TextContent: StrictStr | None = None
    ZipFileContent: StrictBytes | BinaryIO | StrictStr | None = None
    S3ContentLocation: KinesisAnalyticsS3ContentLocation | None = None
