from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsAmazonMqBrokerEncryptionOptionsDetails(BaseModel):
    KmsKeyId: StrictStr | None = None
    UseAwsOwnedKey: StrictBool | None = None
