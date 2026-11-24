from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKKafkaClusterSaslScramAuthentication(BaseModel):
    Mechanism: StrictStr | None = None
    SecretArn: StrictStr | None = None
