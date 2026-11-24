from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_resource_collection_filter import DevOpsGuruResourceCollectionFilter


class DevOpsGuruGetResourceCollectionResponse(BaseModel):
    ResourceCollection: DevOpsGuruResourceCollectionFilter | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
