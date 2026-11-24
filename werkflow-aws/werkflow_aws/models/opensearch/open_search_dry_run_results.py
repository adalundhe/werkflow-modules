from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDryRunResults(BaseModel):
    DeploymentType: StrictStr | None = None
    Message: StrictStr | None = None
