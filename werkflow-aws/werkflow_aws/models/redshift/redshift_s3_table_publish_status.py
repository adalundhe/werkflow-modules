from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftS3TablePublishStatus(BaseModel):
    S3Tables: list[StrictStr] | None = None
    S3TableNamespace: StrictStr | None = None
    S3TableGranularity: StrictStr | None = None
    EnabledAll: StrictBool | None = None
    LastIngestionTimes: dict[StrictStr, StrictStr] | None = None
