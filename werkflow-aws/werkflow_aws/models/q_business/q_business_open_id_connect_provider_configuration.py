from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessOpenIDConnectProviderConfiguration(BaseModel):
    secretsArn: StrictStr | None = None
    secretsRole: StrictStr | None = None
