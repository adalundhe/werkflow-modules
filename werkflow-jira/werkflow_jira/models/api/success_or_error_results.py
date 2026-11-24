from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .remove_field_parameters_result_error import RemoveFieldParametersResultError


class SuccessOrErrorResults(BaseModel):
    error: RemoveFieldParametersResultError | None = None
    fieldId: StrictStr | None = None
    schemeId: StrictInt | None = None
    success: StrictBool | None = None
    workTypeIds: list[StrictInt] | None = None
