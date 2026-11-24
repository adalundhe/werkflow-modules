from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_eks_source import ResilienceHubEksSource
from .resilience_hub_terraform_source import ResilienceHubTerraformSource


class ResilienceHubImportResourcesToDraftAppVersionResponse(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    eksSources: list[ResilienceHubEksSource] | None = None
    sourceArns: list[StrictStr] | None = None
    status: StrictStr | None = None
    terraformSources: list[ResilienceHubTerraformSource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
