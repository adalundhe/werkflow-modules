from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKKafkaClusterOAuthIamJwtBearer(BaseModel):
    Audience: StrictStr | None = None
    SigningAlgorithm: StrictStr | None = None
    TokenRequestSecretArn: StrictStr | None = None
