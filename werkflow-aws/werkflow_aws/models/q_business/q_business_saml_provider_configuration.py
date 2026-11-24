from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessSamlProviderConfiguration(BaseModel):
    authenticationUrl: StrictStr | None = None
