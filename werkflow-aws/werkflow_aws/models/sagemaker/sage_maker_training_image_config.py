from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_training_repository_access_mode import SageMakerTrainingRepositoryAccessMode
from .sage_maker_training_repository_auth_config import SageMakerTrainingRepositoryAuthConfig


class SageMakerTrainingImageConfig(BaseModel):
    TrainingRepositoryAccessMode: SageMakerTrainingRepositoryAccessMode | None = None
    TrainingRepositoryAuthConfig: SageMakerTrainingRepositoryAuthConfig | None = None
