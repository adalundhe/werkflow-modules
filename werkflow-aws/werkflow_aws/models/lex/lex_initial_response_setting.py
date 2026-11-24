from __future__ import annotations
from pydantic import BaseModel
from .lex_conditional_specification import LexConditionalSpecification
from .lex_dialog_code_hook_invocation_setting import LexDialogCodeHookInvocationSetting
from .lex_dialog_state import LexDialogState
from .lex_response_specification import LexResponseSpecification


class LexInitialResponseSetting(BaseModel):
    initialResponse: LexResponseSpecification | None = None
    nextStep: LexDialogState | None = None
    conditional: LexConditionalSpecification | None = None
    codeHook: LexDialogCodeHookInvocationSetting | None = None
