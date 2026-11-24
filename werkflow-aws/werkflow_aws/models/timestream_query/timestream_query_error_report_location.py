from __future__ import annotations
from pydantic import BaseModel
from .timestream_query_s3_report_location import TimestreamQueryS3ReportLocation


class TimestreamQueryErrorReportLocation(BaseModel):
    S3ReportLocation: TimestreamQueryS3ReportLocation | None = None
