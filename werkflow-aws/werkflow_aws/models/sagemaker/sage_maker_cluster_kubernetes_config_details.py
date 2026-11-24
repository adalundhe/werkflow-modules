from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_kubernetes_taint import SageMakerClusterKubernetesTaint


class SageMakerClusterKubernetesConfigDetails(BaseModel):
    CurrentLabels: dict[StrictStr, StrictStr] | None = None
    DesiredLabels: dict[StrictStr, StrictStr] | None = None
    CurrentTaints: list[SageMakerClusterKubernetesTaint] | None = None
    DesiredTaints: list[SageMakerClusterKubernetesTaint] | None = None
