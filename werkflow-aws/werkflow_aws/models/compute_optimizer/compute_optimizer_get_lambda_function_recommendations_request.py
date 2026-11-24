from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_lambda_function_recommendation_filter import ComputeOptimizerLambdaFunctionRecommendationFilter


class ComputeOptimizerGetLambdaFunctionRecommendationsRequest(BaseModel):
    functionArns: list[StrictStr] | None = None
    accountIds: list[StrictStr] | None = None
    filters: list[ComputeOptimizerLambdaFunctionRecommendationFilter] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
