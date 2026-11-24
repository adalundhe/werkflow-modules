from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectContactFlowModuleVersionSummary(BaseModel):
    Arn: StrictStr | None = None
    VersionDescription: StrictStr | None = None
    Version: StrictInt | None = None
