from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_model_compilation_config import SageMakerModelCompilationConfig
from .sage_maker_model_quantization_config import SageMakerModelQuantizationConfig
from .sage_maker_model_sharding_config import SageMakerModelShardingConfig
from .sage_maker_model_speculative_decoding_config import SageMakerModelSpeculativeDecodingConfig


class SageMakerOptimizationConfig(BaseModel):
    ModelQuantizationConfig: SageMakerModelQuantizationConfig | None = None
    ModelCompilationConfig: SageMakerModelCompilationConfig | None = None
    ModelShardingConfig: SageMakerModelShardingConfig | None = None
    ModelSpeculativeDecodingConfig: SageMakerModelSpeculativeDecodingConfig | None = None
