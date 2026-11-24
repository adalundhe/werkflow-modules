from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_eks_source_cluster_namespace import ResilienceHubEksSourceClusterNamespace
from .resilience_hub_terraform_source import ResilienceHubTerraformSource


class ResilienceHubDeleteAppInputSourceRequest(BaseModel):
    appArn: StrictStr
    clientToken: StrictStr | None = None
    eksSourceClusterNamespace: ResilienceHubEksSourceClusterNamespace | None = None
    sourceArn: StrictStr | None = None
    terraformSource: ResilienceHubTerraformSource | None = None
