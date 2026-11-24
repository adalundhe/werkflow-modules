from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_runtime_version_error import LambdaRuntimeVersionError


class LambdaRuntimeVersionConfig(BaseModel):
    RuntimeVersionArn: StrictStr | None = None
    Error: LambdaRuntimeVersionError | None = None
