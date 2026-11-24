from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheSecretManagerAuthConfig(BaseModel):
    SecretArn: StrictStr | None = None
