from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .resilience_hub_eks_source_cluster_namespace import ResilienceHubEksSourceClusterNamespace
from .resilience_hub_terraform_source import ResilienceHubTerraformSource


class ResilienceHubAppInputSource(BaseModel):
    eksSourceClusterNamespace: ResilienceHubEksSourceClusterNamespace | None = None
    importType: StrictStr | None = None
    resourceCount: StrictInt | None = None
    sourceArn: StrictStr | None = None
    sourceName: StrictStr | None = None
    terraformSource: ResilienceHubTerraformSource | None = None
