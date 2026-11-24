from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsValidateStateMachineDefinitionDiagnostic(BaseModel):
    severity: StrictStr | None = None
    code: StrictStr | None = None
    message: StrictStr | None = None
    location: StrictStr | None = None
