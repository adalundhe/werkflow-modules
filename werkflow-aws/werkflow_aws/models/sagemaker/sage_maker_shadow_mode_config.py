from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_shadow_model_variant_config import SageMakerShadowModelVariantConfig


class SageMakerShadowModeConfig(BaseModel):
    SourceModelVariantName: StrictStr | None = None
    ShadowModelVariants: list[SageMakerShadowModelVariantConfig] | None = None
