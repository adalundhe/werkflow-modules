from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_routing_target_async_inference_notification_config import SageMakerRoutingTargetAsyncInferenceNotificationConfig


class SageMakerRoutingTargetAsyncInferenceOutputConfig(BaseModel):
    S3OutputPath: StrictStr | None = None
    S3FailurePath: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    NotificationConfig: SageMakerRoutingTargetAsyncInferenceNotificationConfig | None = None
