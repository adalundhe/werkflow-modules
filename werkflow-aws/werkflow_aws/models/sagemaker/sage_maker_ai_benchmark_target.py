from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_ai_benchmark_endpoint import SageMakerAIBenchmarkEndpoint


class SageMakerAIBenchmarkTarget(BaseModel):
    Endpoint: SageMakerAIBenchmarkEndpoint | None = None
