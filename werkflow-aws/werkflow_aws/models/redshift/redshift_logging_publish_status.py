from __future__ import annotations
from pydantic import BaseModel
from .redshift_s3_table_publish_status import RedshiftS3TablePublishStatus


class RedshiftLoggingPublishStatus(BaseModel):
    S3Tables: RedshiftS3TablePublishStatus | None = None
