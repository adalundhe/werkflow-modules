from __future__ import annotations
from pydantic import BaseModel
from .timestream_write_report_s3_configuration import TimestreamWriteReportS3Configuration


class TimestreamWriteReportConfiguration(BaseModel):
    ReportS3Configuration: TimestreamWriteReportS3Configuration | None = None
