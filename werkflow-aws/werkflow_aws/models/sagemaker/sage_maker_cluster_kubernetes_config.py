from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_kubernetes_taint import SageMakerClusterKubernetesTaint


class SageMakerClusterKubernetesConfig(BaseModel):
    Labels: dict[StrictStr, StrictStr] | None = None
    Taints: list[SageMakerClusterKubernetesTaint] | None = None
