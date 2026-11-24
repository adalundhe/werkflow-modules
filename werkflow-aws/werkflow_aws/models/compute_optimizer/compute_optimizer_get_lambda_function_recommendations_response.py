from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_lambda_function_recommendation import ComputeOptimizerLambdaFunctionRecommendation


class ComputeOptimizerGetLambdaFunctionRecommendationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    lambdaFunctionRecommendations: list[ComputeOptimizerLambdaFunctionRecommendation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
