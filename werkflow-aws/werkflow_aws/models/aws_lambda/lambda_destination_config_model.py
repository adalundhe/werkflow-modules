from __future__ import annotations
from pydantic import BaseModel
from .lambda_on_failure_model import LambdaOnFailureModel
from .lambda_on_success_model import LambdaOnSuccessModel


class LambdaDestinationConfigModel(BaseModel):
    OnSuccess: LambdaOnSuccessModel | None = None
    OnFailure: LambdaOnFailureModel | None = None
