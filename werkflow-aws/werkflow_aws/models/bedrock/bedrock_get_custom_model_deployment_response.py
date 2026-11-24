from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_custom_model_deployment_update_details import BedrockCustomModelDeploymentUpdateDetails


class BedrockGetCustomModelDeploymentResponse(BaseModel):
    customModelDeploymentArn: StrictStr | None = None
    modelDeploymentName: StrictStr | None = None
    modelArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    description: StrictStr | None = None
    updateDetails: BedrockCustomModelDeploymentUpdateDetails | None = None
    failureMessage: StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
