from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexLambdaCodeHook(BaseModel):
    lambdaARN: StrictStr | None = None
    codeHookInterfaceVersion: StrictStr | None = None
