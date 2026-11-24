from __future__ import annotations
from pydantic import BaseModel
from .compute_optimizer_s3_destination import ComputeOptimizerS3Destination


class ComputeOptimizerExportDestination(BaseModel):
    s3: ComputeOptimizerS3Destination | None = None
