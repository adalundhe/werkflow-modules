from __future__ import annotations
from pydantic import BaseModel
from .update_field_scheme_parameters_partial_failure import UpdateFieldSchemeParametersPartialFailure


class UpdateFieldSchemeParametersResponse(BaseModel):
    results: list[UpdateFieldSchemeParametersPartialFailure] | None = None
