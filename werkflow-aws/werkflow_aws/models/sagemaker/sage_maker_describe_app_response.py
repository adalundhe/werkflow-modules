from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerDescribeAppResponse(BaseModel):
    AppArn: StrictStr | None = None
    AppType: StrictStr | None = None
    AppName: StrictStr | None = None
    DomainId: StrictStr | None = None
    UserProfileName: StrictStr | None = None
    SpaceName: StrictStr | None = None
    Status: StrictStr | None = None
    EffectiveTrustedIdentityPropagationStatus: StrictStr | None = None
    RecoveryMode: StrictBool | None = None
    LastHealthCheckTimestamp: datetime.datetime | StrictStr | None = None
    LastUserActivityTimestamp: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    ResourceSpec: SageMakerResourceSpec | None = None
    BuiltInLifecycleConfigArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
