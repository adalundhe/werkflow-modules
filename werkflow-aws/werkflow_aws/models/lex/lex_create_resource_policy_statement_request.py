from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lex_principal import LexPrincipal


class LexCreateResourcePolicyStatementRequest(BaseModel):
    resourceArn: StrictStr
    statementId: StrictStr
    effect: Literal['Allow', 'Deny']
    principal: list[LexPrincipal]
    action: list[StrictStr]
    condition: dict[StrictStr, dict[StrictStr, StrictStr]] | None = None
    expectedRevisionId: StrictStr | None = None
