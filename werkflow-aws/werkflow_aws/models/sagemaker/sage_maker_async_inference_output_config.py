from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_async_inference_notification_config import SageMakerAsyncInferenceNotificationConfig


class SageMakerAsyncInferenceOutputConfig(BaseModel):
    KmsKeyId: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
    NotificationConfig: SageMakerAsyncInferenceNotificationConfig | None = None
    S3FailurePath: StrictStr | None = None
