from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_clarify_explainer_config import SageMakerClarifyExplainerConfig


class SageMakerExplainerConfig(BaseModel):
    ClarifyExplainerConfig: SageMakerClarifyExplainerConfig | None = None
