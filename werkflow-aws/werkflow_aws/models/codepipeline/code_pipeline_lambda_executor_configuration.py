from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineLambdaExecutorConfiguration(BaseModel):
    lambdaFunctionArn: StrictStr | None = None
