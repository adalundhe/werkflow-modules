from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_cloud_formation_collection import DevOpsGuruCloudFormationCollection
from .dev_ops_guru_tag_collection import DevOpsGuruTagCollection


class DevOpsGuruResourceCollection(BaseModel):
    CloudFormation: DevOpsGuruCloudFormationCollection | None = None
    Tags: list[DevOpsGuruTagCollection] | None = None
