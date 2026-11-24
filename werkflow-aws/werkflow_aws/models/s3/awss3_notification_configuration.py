from __future__ import annotations
from pydantic import BaseModel
from .awss3_event_bridge_configuration_input import AWSS3EventBridgeConfigurationInput
from .awss3_lambda_function_configuration_input import AWSS3LambdaFunctionConfigurationInput
from .awss3_queue_configuration_input import AWSS3QueueConfigurationInput
from .awss3_topic_configuration_input import AWSS3TopicConfigurationInput


class AWSS3NotificationConfiguration(BaseModel):
    TopicConfigurations: list[AWSS3TopicConfigurationInput] | None = None
    QueueConfigurations: list[AWSS3QueueConfigurationInput] | None = None
    LambdaFunctionConfigurations: list[AWSS3LambdaFunctionConfigurationInput] | None = None
    EventBridgeConfiguration: AWSS3EventBridgeConfigurationInput | None = None
