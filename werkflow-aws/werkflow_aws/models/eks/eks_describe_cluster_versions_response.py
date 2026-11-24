from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_cluster_version_information import EKSClusterVersionInformation


class EKSDescribeClusterVersionsResponse(BaseModel):
    nextToken: StrictStr | None = None
    clusterVersions: list[EKSClusterVersionInformation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
