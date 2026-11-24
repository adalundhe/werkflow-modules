from __future__ import annotations
from pydantic import BaseModel
from .success_or_error_results import SuccessOrErrorResults


class RemoveFieldParametersResult(BaseModel):
    results: list[SuccessOrErrorResults] | None = None
