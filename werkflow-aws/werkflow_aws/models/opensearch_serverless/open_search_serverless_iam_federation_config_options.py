from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessIamFederationConfigOptions(BaseModel):
    groupAttribute: StrictStr | None = None
    userAttribute: StrictStr | None = None
