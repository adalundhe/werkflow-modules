from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerAuthenticationConfiguration(BaseModel):
    ConnectionArn: StrictStr | None = None
    AccessRoleArn: StrictStr | None = None
