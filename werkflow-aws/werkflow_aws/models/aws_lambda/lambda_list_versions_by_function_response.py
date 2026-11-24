from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_function_configuration import LambdaFunctionConfiguration


class LambdaListVersionsByFunctionResponse(BaseModel):
    NextMarker: StrictStr | None = None
    Versions: list[LambdaFunctionConfiguration] | None = None
