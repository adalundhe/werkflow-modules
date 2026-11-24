from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerCertificateValidationRecord(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Value: StrictStr | None = None
    Status: StrictStr | None = None
