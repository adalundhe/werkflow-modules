from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .quick_sight_space_quick_sight_resource_details import QuickSightSpaceQuickSightResourceDetails


class QuickSightSpaceResourceOperation(BaseModel):
    ResourceType: Literal['TOPIC', 'DASHBOARD', 'KNOWLEDGE_BASE', 'ACTION_CONNECTOR', 'DATA_SET']
    ResourceDetails: QuickSightSpaceQuickSightResourceDetails
