from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_training_repository_auth_config_model import SageMakerTrainingRepositoryAuthConfigModel


class SageMakerTrainingImageConfigModel(BaseModel):
    TrainingRepositoryAccessMode: StrictStr | None = None
    TrainingRepositoryAuthConfig: SageMakerTrainingRepositoryAuthConfigModel | None = None
