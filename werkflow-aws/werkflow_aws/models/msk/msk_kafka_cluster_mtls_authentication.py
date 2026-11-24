from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKKafkaClusterMTLSAuthentication(BaseModel):
    SecretArn: StrictStr | None = None
