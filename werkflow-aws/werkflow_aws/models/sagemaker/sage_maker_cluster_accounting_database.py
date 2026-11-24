from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerClusterAccountingDatabase(BaseModel):
    Endpoint: StrictStr | None = None
    Port: StrictInt | None = None
    Name: StrictStr | None = None
    SecretArn: StrictStr | None = None
