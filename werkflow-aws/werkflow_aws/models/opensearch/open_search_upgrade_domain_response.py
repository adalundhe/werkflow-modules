from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_change_progress_details import OpenSearchChangeProgressDetails
from .open_search_deployment_strategy_override_options import OpenSearchDeploymentStrategyOverrideOptions


class OpenSearchUpgradeDomainResponse(BaseModel):
    UpgradeId: StrictStr | None = None
    DomainName: StrictStr | None = None
    TargetVersion: StrictStr | None = None
    PerformCheckOnly: StrictBool | None = None
    AdvancedOptions: dict[StrictStr, StrictStr] | None = None
    DeploymentStrategyOptions: OpenSearchDeploymentStrategyOverrideOptions | None = None
    ChangeProgressDetails: OpenSearchChangeProgressDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
