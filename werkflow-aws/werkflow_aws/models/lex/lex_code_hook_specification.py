from __future__ import annotations
from pydantic import BaseModel
from .lex_lambda_code_hook import LexLambdaCodeHook


class LexCodeHookSpecification(BaseModel):
    lambdaCodeHook: LexLambdaCodeHook | None = None
