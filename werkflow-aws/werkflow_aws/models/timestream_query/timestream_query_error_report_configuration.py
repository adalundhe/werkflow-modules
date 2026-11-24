from __future__ import annotations
from pydantic import BaseModel
from .timestream_query_s3_configuration import TimestreamQueryS3Configuration


class TimestreamQueryErrorReportConfiguration(BaseModel):
    S3Configuration: TimestreamQueryS3Configuration | None = None
