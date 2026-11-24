from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsElasticsearchDomainNodeToNodeEncryptionOptions(BaseModel):
    Enabled: StrictBool | None = None
