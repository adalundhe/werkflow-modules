from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_container_metrics_config_model import SageMakerContainerMetricsConfigModel


class SageMakerInferenceComponentContainerSpecification(BaseModel):
    Image: StrictStr | None = None
    ArtifactUrl: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    ContainerMetricsConfig: SageMakerContainerMetricsConfigModel | None = None
