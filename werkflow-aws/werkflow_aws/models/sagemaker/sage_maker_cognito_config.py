from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCognitoConfig(BaseModel):
    UserPool: StrictStr | None = None
    ClientId: StrictStr | None = None
