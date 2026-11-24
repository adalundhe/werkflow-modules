from __future__ import annotations
from pydantic import BaseModel
from .open_search_deployment_strategy_options import OpenSearchDeploymentStrategyOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchDeploymentStrategyOptionsStatus(BaseModel):
    Options: OpenSearchDeploymentStrategyOptions | None = None
    Status: OpenSearchOptionStatus | None = None
