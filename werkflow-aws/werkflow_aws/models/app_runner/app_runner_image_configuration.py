from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerImageConfiguration(BaseModel):
    RuntimeEnvironmentVariables: dict[StrictStr, StrictStr] | None = None
    StartCommand: StrictStr | None = None
    Port: StrictStr | None = None
    RuntimeEnvironmentSecrets: dict[StrictStr, StrictStr] | None = None
