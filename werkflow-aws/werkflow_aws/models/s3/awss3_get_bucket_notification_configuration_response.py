from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_event_bridge_configuration import AWSS3EventBridgeConfiguration
from .awss3_lambda_function_configuration import AWSS3LambdaFunctionConfiguration
from .awss3_queue_configuration import AWSS3QueueConfiguration
from .awss3_topic_configuration import AWSS3TopicConfiguration


class AWSS3GetBucketNotificationConfigurationResponse(BaseModel):
    TopicConfigurations: list[AWSS3TopicConfiguration] | None = None
    QueueConfigurations: list[AWSS3QueueConfiguration] | None = None
    LambdaFunctionConfigurations: list[AWSS3LambdaFunctionConfiguration] | None = None
    EventBridgeConfiguration: AWSS3EventBridgeConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
