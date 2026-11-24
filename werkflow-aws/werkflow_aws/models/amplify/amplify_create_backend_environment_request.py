from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyCreateBackendEnvironmentRequest(BaseModel):
    appId: StrictStr
    environmentName: StrictStr
    stackName: StrictStr | None = None
    deploymentArtifacts: StrictStr | None = None
