from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsCodeBuildProjectLogsConfigS3LogsDetails(BaseModel):
    EncryptionDisabled: StrictBool | None = None
    Location: StrictStr | None = None
    Status: StrictStr | None = None
