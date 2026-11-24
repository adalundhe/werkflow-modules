from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_exposure_finding import SecurityHubExposureFinding
from .security_hub_remediation_resource import SecurityHubRemediationResource
from .security_hub_remediation_trait import SecurityHubRemediationTrait


class SecurityHubListExposuresByRemediationV2Response(BaseModel):
    Items: list[SecurityHubExposureFinding] | None = None
    TargetUid: StrictStr | None = None
    Resource: SecurityHubRemediationResource | None = None
    TotalCount: StrictInt | None = None
    Trait: SecurityHubRemediationTrait | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
