from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsEcrRepositoryImageScanningConfigurationDetails(BaseModel):
    ScanOnPush: StrictBool | None = None
