from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .step_functions_validate_state_machine_definition_diagnostic import StepFunctionsValidateStateMachineDefinitionDiagnostic


class StepFunctionsValidateStateMachineDefinitionResponse(BaseModel):
    result: StrictStr | None = None
    diagnostics: list[StepFunctionsValidateStateMachineDefinitionDiagnostic] | None = None
    truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
