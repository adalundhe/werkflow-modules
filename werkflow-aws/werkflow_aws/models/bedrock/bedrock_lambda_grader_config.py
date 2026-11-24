from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockLambdaGraderConfig(BaseModel):
    lambdaArn: StrictStr | None = None
