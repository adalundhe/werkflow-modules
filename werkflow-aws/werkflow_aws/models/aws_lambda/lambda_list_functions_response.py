from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_function_configuration import LambdaFunctionConfiguration


class LambdaListFunctionsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    Functions: list[LambdaFunctionConfiguration] | None = None
