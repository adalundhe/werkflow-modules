from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .kinesis_analytics_s3_content_location_update import KinesisAnalyticsS3ContentLocationUpdate


class KinesisAnalyticsCodeContentUpdate(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    TextContentUpdate: StrictStr | None = None
    ZipFileContentUpdate: StrictBytes | BinaryIO | StrictStr | None = None
    S3ContentLocationUpdate: KinesisAnalyticsS3ContentLocationUpdate | None = None
