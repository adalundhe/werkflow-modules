from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_cloned_blue_green_options import OpenSearchClonedBlueGreenOptions


class OpenSearchDeploymentStrategyOverrideOptions(BaseModel):
    DeploymentStrategy: StrictStr | None = None
    ClonedBlueGreenOptions: OpenSearchClonedBlueGreenOptions | None = None
