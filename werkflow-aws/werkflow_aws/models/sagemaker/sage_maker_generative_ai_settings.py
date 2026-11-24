from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerGenerativeAiSettings(BaseModel):
    AmazonBedrockRoleArn: StrictStr | None = None
