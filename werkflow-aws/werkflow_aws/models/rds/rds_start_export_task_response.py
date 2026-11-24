from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class RDSStartExportTaskResponse(BaseModel):
    ExportTaskIdentifier: StrictStr | None = None
    SourceArn: StrictStr | None = None
    ExportOnly: list[StrictStr] | None = None
    SnapshotTime: datetime.datetime | StrictStr | None = None
    TaskStartTime: datetime.datetime | StrictStr | None = None
    TaskEndTime: datetime.datetime | StrictStr | None = None
    S3Bucket: StrictStr | None = None
    S3Prefix: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Status: StrictStr | None = None
    PercentProgress: StrictInt | None = None
    TotalExtractedDataInGB: StrictInt | None = None
    FailureCause: StrictStr | None = None
    WarningMessage: StrictStr | None = None
    SourceType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
