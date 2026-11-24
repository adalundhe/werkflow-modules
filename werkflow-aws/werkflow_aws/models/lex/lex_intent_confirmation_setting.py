from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_conditional_specification import LexConditionalSpecification
from .lex_dialog_code_hook_invocation_setting import LexDialogCodeHookInvocationSetting
from .lex_dialog_state import LexDialogState
from .lex_elicitation_code_hook_invocation_setting import LexElicitationCodeHookInvocationSetting
from .lex_prompt_specification import LexPromptSpecification
from .lex_response_specification import LexResponseSpecification


class LexIntentConfirmationSetting(BaseModel):
    promptSpecification: LexPromptSpecification | None = None
    declinationResponse: LexResponseSpecification | None = None
    active: StrictBool | None = None
    confirmationResponse: LexResponseSpecification | None = None
    confirmationNextStep: LexDialogState | None = None
    confirmationConditional: LexConditionalSpecification | None = None
    declinationNextStep: LexDialogState | None = None
    declinationConditional: LexConditionalSpecification | None = None
    failureResponse: LexResponseSpecification | None = None
    failureNextStep: LexDialogState | None = None
    failureConditional: LexConditionalSpecification | None = None
    codeHook: LexDialogCodeHookInvocationSetting | None = None
    elicitationCodeHook: LexElicitationCodeHookInvocationSetting | None = None
