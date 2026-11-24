from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_s3_destination import ComputeOptimizerS3Destination


class ComputeOptimizerExportLambdaFunctionRecommendationsResponse(BaseModel):
    jobId: StrictStr | None = None
    s3Destination: ComputeOptimizerS3Destination | None = None
    ResponseMetadata: dict[str, Any] | None = None
