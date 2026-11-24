from __future__ import annotations
from pydantic import BaseModel
from .timestream_write_s3_configuration import TimestreamWriteS3Configuration


class TimestreamWriteMagneticStoreRejectedDataLocation(BaseModel):
    S3Configuration: TimestreamWriteS3Configuration | None = None
