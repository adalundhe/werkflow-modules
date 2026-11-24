from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerEgressConfiguration(BaseModel):
    EgressType: StrictStr | None = None
    VpcConnectorArn: StrictStr | None = None
