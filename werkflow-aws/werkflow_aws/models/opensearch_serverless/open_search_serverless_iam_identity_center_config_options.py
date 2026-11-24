from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessIamIdentityCenterConfigOptions(BaseModel):
    instanceArn: StrictStr | None = None
    applicationArn: StrictStr | None = None
    applicationName: StrictStr | None = None
    applicationDescription: StrictStr | None = None
    userAttribute: StrictStr | None = None
    groupAttribute: StrictStr | None = None
