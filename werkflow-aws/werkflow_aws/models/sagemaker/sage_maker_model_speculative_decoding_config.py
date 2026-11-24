from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_speculative_decoding_training_data_source import SageMakerModelSpeculativeDecodingTrainingDataSource


class SageMakerModelSpeculativeDecodingConfig(BaseModel):
    Technique: StrictStr | None = None
    TrainingDataSource: SageMakerModelSpeculativeDecodingTrainingDataSource | None = None
