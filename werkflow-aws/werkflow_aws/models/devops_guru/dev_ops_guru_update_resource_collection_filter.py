from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_update_cloud_formation_collection_filter import DevOpsGuruUpdateCloudFormationCollectionFilter
from .dev_ops_guru_update_tag_collection_filter import DevOpsGuruUpdateTagCollectionFilter


class DevOpsGuruUpdateResourceCollectionFilter(BaseModel):
    CloudFormation: DevOpsGuruUpdateCloudFormationCollectionFilter | None = None
    Tags: list[DevOpsGuruUpdateTagCollectionFilter] | None = None
