from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceConfigurationRecorderSummary(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    servicePrincipal: StrictStr | None = None
    recordingScope: StrictStr | None = None
    provider: StrictStr | None = None
