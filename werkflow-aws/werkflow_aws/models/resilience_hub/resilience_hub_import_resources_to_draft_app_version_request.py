from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .resilience_hub_eks_source import ResilienceHubEksSource
from .resilience_hub_terraform_source import ResilienceHubTerraformSource


class ResilienceHubImportResourcesToDraftAppVersionRequest(BaseModel):
    appArn: StrictStr
    eksSources: list[ResilienceHubEksSource] | None = None
    importStrategy: Literal['AddOnly', 'ReplaceAll'] | None = None
    sourceArns: list[StrictStr] | None = None
    terraformSources: list[ResilienceHubTerraformSource] | None = None
