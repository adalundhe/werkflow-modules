from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSStartExportTaskRequest(BaseModel):
    ExportTaskIdentifier: StrictStr
    SourceArn: StrictStr
    S3BucketName: StrictStr
    IamRoleArn: StrictStr
    KmsKeyId: StrictStr
    S3Prefix: StrictStr | None = None
    ExportOnly: list[StrictStr] | None = None
