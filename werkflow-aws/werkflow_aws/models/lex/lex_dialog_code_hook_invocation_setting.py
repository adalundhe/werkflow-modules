from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lex_post_dialog_code_hook_invocation_specification import LexPostDialogCodeHookInvocationSpecification


class LexDialogCodeHookInvocationSetting(BaseModel):
    enableCodeHookInvocation: StrictBool | None = None
    active: StrictBool | None = None
    invocationLabel: StrictStr | None = None
    postCodeHookSpecification: LexPostDialogCodeHookInvocationSpecification | None = None
