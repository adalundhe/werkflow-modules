from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerCodeConfigurationValues(BaseModel):
    Runtime: StrictStr | None = None
    BuildCommand: StrictStr | None = None
    StartCommand: StrictStr | None = None
    Port: StrictStr | None = None
    RuntimeEnvironmentVariables: dict[StrictStr, StrictStr] | None = None
    RuntimeEnvironmentSecrets: dict[StrictStr, StrictStr] | None = None
