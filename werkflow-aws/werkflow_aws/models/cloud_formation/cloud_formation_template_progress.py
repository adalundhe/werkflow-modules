from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudFormationTemplateProgress(BaseModel):
    ResourcesSucceeded: StrictInt | None = None
    ResourcesFailed: StrictInt | None = None
    ResourcesProcessing: StrictInt | None = None
    ResourcesPending: StrictInt | None = None
