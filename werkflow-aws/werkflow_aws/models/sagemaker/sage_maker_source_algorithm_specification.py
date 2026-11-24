from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_source_algorithm import SageMakerSourceAlgorithm


class SageMakerSourceAlgorithmSpecification(BaseModel):
    SourceAlgorithms: list[SageMakerSourceAlgorithm] | None = None
