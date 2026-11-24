from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeCodeRepositoryRequest(BaseModel):
    CodeRepositoryName: StrictStr
