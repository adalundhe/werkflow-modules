from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_project_data_retention import BedrockProjectDataRetention


class BedrockUpdateProjectRequest(BaseModel):
    projectIdentifier: StrictStr
    name: StrictStr | None = None
    dataRetention: BedrockProjectDataRetention | None = None
