from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails(BaseModel):
    Enabled: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
