from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerSourceCodeVersion(BaseModel):
    Type: StrictStr | None = None
    Value: StrictStr | None = None
