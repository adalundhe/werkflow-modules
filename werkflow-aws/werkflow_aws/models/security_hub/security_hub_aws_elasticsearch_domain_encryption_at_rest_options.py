from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsElasticsearchDomainEncryptionAtRestOptions(BaseModel):
    Enabled: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
