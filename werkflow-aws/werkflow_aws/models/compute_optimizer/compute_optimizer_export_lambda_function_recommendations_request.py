from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .compute_optimizer_lambda_function_recommendation_filter import ComputeOptimizerLambdaFunctionRecommendationFilter
from .compute_optimizer_s3_destination_config import ComputeOptimizerS3DestinationConfig


class ComputeOptimizerExportLambdaFunctionRecommendationsRequest(BaseModel):
    s3DestinationConfig: ComputeOptimizerS3DestinationConfig
    accountIds: list[StrictStr] | None = None
    filters: list[ComputeOptimizerLambdaFunctionRecommendationFilter] | None = None
    fieldsToExport: list[StrictStr] | None = None
    fileFormat: Literal['Csv'] | None = None
    includeMemberAccounts: StrictBool | None = None
