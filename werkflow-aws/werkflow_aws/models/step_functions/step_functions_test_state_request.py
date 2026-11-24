from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .step_functions_mock_input import StepFunctionsMockInput
from .step_functions_test_state_configuration import StepFunctionsTestStateConfiguration


class StepFunctionsTestStateRequest(BaseModel):
    definition: StrictStr
    roleArn: StrictStr | None = None
    input: StrictStr | None = None
    inspectionLevel: Literal['INFO', 'DEBUG', 'TRACE'] | None = None
    revealSecrets: StrictBool | None = None
    variables: StrictStr | None = None
    stateName: StrictStr | None = None
    mock: StepFunctionsMockInput | None = None
    context: StrictStr | None = None
    stateConfiguration: StepFunctionsTestStateConfiguration | None = None
