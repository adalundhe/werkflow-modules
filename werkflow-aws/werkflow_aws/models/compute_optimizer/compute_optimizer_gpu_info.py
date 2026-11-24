from __future__ import annotations
from pydantic import BaseModel
from .compute_optimizer_gpu import ComputeOptimizerGpu


class ComputeOptimizerGpuInfo(BaseModel):
    gpus: list[ComputeOptimizerGpu] | None = None
