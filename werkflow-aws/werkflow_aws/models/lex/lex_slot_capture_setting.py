from __future__ import annotations
from pydantic import BaseModel
from .lex_conditional_specification import LexConditionalSpecification
from .lex_dialog_code_hook_invocation_setting import LexDialogCodeHookInvocationSetting
from .lex_dialog_state import LexDialogState
from .lex_elicitation_code_hook_invocation_setting import LexElicitationCodeHookInvocationSetting
from .lex_response_specification import LexResponseSpecification


class LexSlotCaptureSetting(BaseModel):
    captureResponse: LexResponseSpecification | None = None
    captureNextStep: LexDialogState | None = None
    captureConditional: LexConditionalSpecification | None = None
    failureResponse: LexResponseSpecification | None = None
    failureNextStep: LexDialogState | None = None
    failureConditional: LexConditionalSpecification | None = None
    codeHook: LexDialogCodeHookInvocationSetting | None = None
    elicitationCodeHook: LexElicitationCodeHookInvocationSetting | None = None
