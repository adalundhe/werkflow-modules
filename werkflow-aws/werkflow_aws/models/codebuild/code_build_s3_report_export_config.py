from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildS3ReportExportConfig(BaseModel):
    bucket: StrictStr | None = None
    bucketOwner: StrictStr | None = None
    path: StrictStr | None = None
    packaging: StrictStr | None = None
    encryptionKey: StrictStr | None = None
    encryptionDisabled: StrictBool | None = None
