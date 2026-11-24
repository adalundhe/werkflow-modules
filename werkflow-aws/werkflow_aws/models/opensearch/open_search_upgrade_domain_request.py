from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_deployment_strategy_override_options import OpenSearchDeploymentStrategyOverrideOptions


class OpenSearchUpgradeDomainRequest(BaseModel):
    DomainName: StrictStr
    TargetVersion: StrictStr
    PerformCheckOnly: StrictBool | None = None
    AdvancedOptions: dict[StrictStr, StrictStr] | None = None
    DeploymentStrategyOptions: OpenSearchDeploymentStrategyOverrideOptions | None = None
