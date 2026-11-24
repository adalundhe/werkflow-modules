from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_cloud_function_configuration import AWSS3CloudFunctionConfiguration
from .awss3_queue_configuration_deprecated import AWSS3QueueConfigurationDeprecated
from .awss3_topic_configuration_deprecated import AWSS3TopicConfigurationDeprecated


class AWSS3GetBucketNotificationResponse(BaseModel):
    TopicConfiguration: AWSS3TopicConfigurationDeprecated | None = None
    QueueConfiguration: AWSS3QueueConfigurationDeprecated | None = None
    CloudFunctionConfiguration: AWSS3CloudFunctionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
