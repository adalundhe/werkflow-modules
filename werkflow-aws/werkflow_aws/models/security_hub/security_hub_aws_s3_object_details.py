from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3ObjectDetails(BaseModel):
    LastModified: StrictStr | None = None
    ETag: StrictStr | None = None
    VersionId: StrictStr | None = None
    ContentType: StrictStr | None = None
    ServerSideEncryption: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
