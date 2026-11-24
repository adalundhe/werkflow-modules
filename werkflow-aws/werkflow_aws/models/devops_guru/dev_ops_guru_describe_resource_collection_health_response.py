from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_cloud_formation_health import DevOpsGuruCloudFormationHealth
from .dev_ops_guru_service_health import DevOpsGuruServiceHealth
from .dev_ops_guru_tag_health import DevOpsGuruTagHealth


class DevOpsGuruDescribeResourceCollectionHealthResponse(BaseModel):
    CloudFormation: list[DevOpsGuruCloudFormationHealth] | None = None
    Service: list[DevOpsGuruServiceHealth] | None = None
    NextToken: StrictStr | None = None
    Tags: list[DevOpsGuruTagHealth] | None = None
    ResponseMetadata: dict[str, Any] | None = None
