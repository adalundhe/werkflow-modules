from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightDescribeTopicPermissionsV2Response(BaseModel):
    TopicId: StrictStr | None = None
    TopicArn: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
