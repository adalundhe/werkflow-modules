from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessSamlConfigOptions(BaseModel):
    metadata: StrictStr | None = None
    userAttribute: StrictStr | None = None
    groupAttribute: StrictStr | None = None
    openSearchServerlessEntityId: StrictStr | None = None
    sessionTimeout: StrictInt | None = None
