from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsDynamoDbTableSseDescription(BaseModel):
    InaccessibleEncryptionDateTime: StrictStr | None = None
    Status: StrictStr | None = None
    SseType: StrictStr | None = None
    KmsMasterKeyArn: StrictStr | None = None
