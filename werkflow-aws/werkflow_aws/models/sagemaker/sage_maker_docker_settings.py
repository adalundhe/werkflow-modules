from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDockerSettings(BaseModel):
    EnableDockerAccess: StrictStr | None = None
    VpcOnlyTrustedAccounts: list[StrictStr] | None = None
    RootlessDocker: StrictStr | None = None
