from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildS3LogsConfig(BaseModel):
    status: StrictStr | None = None
    location: StrictStr | None = None
    encryptionDisabled: StrictBool | None = None
    bucketOwnerAccess: StrictStr | None = None
