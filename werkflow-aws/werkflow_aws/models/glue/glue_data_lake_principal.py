from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDataLakePrincipal(BaseModel):
    DataLakePrincipalIdentifier: StrictStr | None = None
