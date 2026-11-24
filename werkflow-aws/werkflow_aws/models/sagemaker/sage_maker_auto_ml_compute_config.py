from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_emr_serverless_compute_config import SageMakerEmrServerlessComputeConfig


class SageMakerAutoMLComputeConfig(BaseModel):
    EmrServerlessComputeConfig: SageMakerEmrServerlessComputeConfig | None = None
