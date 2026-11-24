from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_cloud_formation_collection_filter import DevOpsGuruCloudFormationCollectionFilter
from .dev_ops_guru_tag_collection_filter import DevOpsGuruTagCollectionFilter


class DevOpsGuruResourceCollectionFilter(BaseModel):
    CloudFormation: DevOpsGuruCloudFormationCollectionFilter | None = None
    Tags: list[DevOpsGuruTagCollectionFilter] | None = None
