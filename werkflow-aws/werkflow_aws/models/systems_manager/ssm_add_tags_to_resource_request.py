from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ssm_tag import SSMTag


class SSMAddTagsToResourceRequest(BaseModel):
    ResourceType: Literal['Document', 'ManagedInstance', 'MaintenanceWindow', 'Parameter', 'PatchBaseline', 'OpsItem', 'OpsMetadata', 'Automation', 'Association', 'CloudConnector']
    ResourceId: StrictStr
    Tags: list[SSMTag]
