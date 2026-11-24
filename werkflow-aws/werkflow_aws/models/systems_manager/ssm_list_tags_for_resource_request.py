from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMListTagsForResourceRequest(BaseModel):
    ResourceType: Literal['Document', 'ManagedInstance', 'MaintenanceWindow', 'Parameter', 'PatchBaseline', 'OpsItem', 'OpsMetadata', 'Automation', 'Association', 'CloudConnector']
    ResourceId: StrictStr
