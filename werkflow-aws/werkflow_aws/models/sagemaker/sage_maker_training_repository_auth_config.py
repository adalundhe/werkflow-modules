from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTrainingRepositoryAuthConfig(BaseModel):
    TrainingRepositoryCredentialsProviderArn: StrictStr | None = None
