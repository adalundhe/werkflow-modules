from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .dev_ops_guru_update_resource_collection_filter import DevOpsGuruUpdateResourceCollectionFilter


class DevOpsGuruUpdateResourceCollectionRequest(BaseModel):
    Action: Literal['ADD', 'REMOVE']
    ResourceCollection: DevOpsGuruUpdateResourceCollectionFilter
