from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AmplifyBackendEnvironment(BaseModel):
    backendEnvironmentArn: StrictStr | None = None
    environmentName: StrictStr | None = None
    stackName: StrictStr | None = None
    deploymentArtifacts: StrictStr | None = None
    createTime: datetime.datetime | StrictStr | None = None
    updateTime: datetime.datetime | StrictStr | None = None
