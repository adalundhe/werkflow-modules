from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCognitoMemberDefinition(BaseModel):
    UserPool: StrictStr | None = None
    UserGroup: StrictStr | None = None
    ClientId: StrictStr | None = None
