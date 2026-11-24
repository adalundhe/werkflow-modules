from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSExpressGatewayRepositoryCredentials(BaseModel):
    credentialsParameter: StrictStr | None = None
