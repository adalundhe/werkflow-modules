from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_container_metrics_config_model import SageMakerContainerMetricsConfigModel
from .sage_maker_deployed_image_model import SageMakerDeployedImageModel


class SageMakerInferenceComponentContainerSpecificationSummary(BaseModel):
    DeployedImage: SageMakerDeployedImageModel | None = None
    ArtifactUrl: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    ContainerMetricsConfig: SageMakerContainerMetricsConfigModel | None = None
