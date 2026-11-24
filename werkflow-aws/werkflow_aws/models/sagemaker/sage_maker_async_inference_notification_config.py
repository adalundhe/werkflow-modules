from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_async_notification_topic_types import SageMakerAsyncNotificationTopicTypes


class SageMakerAsyncInferenceNotificationConfig(BaseModel):
    SuccessTopic: StrictStr | None = None
    ErrorTopic: StrictStr | None = None
    IncludeInferenceResponseIn: list[SageMakerAsyncNotificationTopicTypes] | None = None
