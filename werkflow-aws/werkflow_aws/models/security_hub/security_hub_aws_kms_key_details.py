from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class SecurityHubAwsKmsKeyDetails(BaseModel):
    AWSAccountId: StrictStr | None = None
    CreationDate: StrictFloat | StrictInt | None = None
    KeyId: StrictStr | None = None
    KeyManager: StrictStr | None = None
    KeyState: StrictStr | None = None
    Origin: StrictStr | None = None
    Description: StrictStr | None = None
    KeyRotationStatus: StrictBool | None = None
