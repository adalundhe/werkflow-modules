from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKKafkaClusterOAuthClientCredentials(BaseModel):
    TokenRequestSecretArn: StrictStr | None = None
