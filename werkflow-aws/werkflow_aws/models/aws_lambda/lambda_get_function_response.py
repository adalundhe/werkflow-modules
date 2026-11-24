from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_concurrency import LambdaConcurrency
from .lambda_function_code_location import LambdaFunctionCodeLocation
from .lambda_function_configuration import LambdaFunctionConfiguration
from .lambda_tags_error import LambdaTagsError


class LambdaGetFunctionResponse(BaseModel):
    Configuration: LambdaFunctionConfiguration | None = None
    Code: LambdaFunctionCodeLocation | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    TagsError: LambdaTagsError | None = None
    Concurrency: LambdaConcurrency | None = None
