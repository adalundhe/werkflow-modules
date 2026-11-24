from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_annotation import CloudFormationAnnotation
from .cloud_formation_hook_target import CloudFormationHookTarget


class CloudFormationGetHookResultResponse(BaseModel):
    HookResultId: StrictStr | None = None
    InvocationPoint: StrictStr | None = None
    FailureMode: StrictStr | None = None
    TypeName: StrictStr | None = None
    OriginalTypeName: StrictStr | None = None
    TypeVersionId: StrictStr | None = None
    TypeConfigurationVersionId: StrictStr | None = None
    TypeArn: StrictStr | None = None
    Status: StrictStr | None = None
    HookStatusReason: StrictStr | None = None
    InvokedAt: datetime.datetime | StrictStr | None = None
    Target: CloudFormationHookTarget | None = None
    Annotations: list[CloudFormationAnnotation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
