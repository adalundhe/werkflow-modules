from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3BucketServerSideEncryptionByDefault(BaseModel):
    SSEAlgorithm: StrictStr | None = None
    KMSMasterKeyID: StrictStr | None = None
