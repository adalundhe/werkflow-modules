from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lambda_amazon_managed_kafka_event_source_config import LambdaAmazonManagedKafkaEventSourceConfig
from .lambda_destination_config import LambdaDestinationConfig
from .lambda_document_db_event_source_config import LambdaDocumentDBEventSourceConfig
from .lambda_event_source_mapping_logging_config import LambdaEventSourceMappingLoggingConfig
from .lambda_event_source_mapping_metrics_config import LambdaEventSourceMappingMetricsConfig
from .lambda_event_source_position import LambdaEventSourcePosition
from .lambda_filter_criteria import LambdaFilterCriteria
from .lambda_function_response_type import LambdaFunctionResponseType
from .lambda_provisioned_poller_config import LambdaProvisionedPollerConfig
from .lambda_scaling_config import LambdaScalingConfig
from .lambda_self_managed_event_source import LambdaSelfManagedEventSource
from .lambda_self_managed_kafka_event_source_config import LambdaSelfManagedKafkaEventSourceConfig
from .lambda_source_access_configuration import LambdaSourceAccessConfiguration


class LambdaCreateEventSourceMappingRequest(BaseModel):
    FunctionName: StrictStr
    EventSourceArn: StrictStr | None = None
    Enabled: StrictBool | None = None
    BatchSize: StrictInt | None = None
    FilterCriteria: LambdaFilterCriteria | None = None
    KMSKeyArn: StrictStr | None = None
    MetricsConfig: LambdaEventSourceMappingMetricsConfig | None = None
    LoggingConfig: LambdaEventSourceMappingLoggingConfig | None = None
    ScalingConfig: LambdaScalingConfig | None = None
    MaximumBatchingWindowInSeconds: StrictInt | None = None
    ParallelizationFactor: StrictInt | None = None
    StartingPosition: LambdaEventSourcePosition | None = None
    StartingPositionTimestamp: datetime.datetime | None = None
    DestinationConfig: LambdaDestinationConfig | None = None
    MaximumRecordAgeInSeconds: StrictInt | None = None
    BisectBatchOnFunctionError: StrictBool | None = None
    MaximumRetryAttempts: StrictInt | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    TumblingWindowInSeconds: StrictInt | None = None
    Topics: list[StrictStr] | None = None
    Queues: list[StrictStr] | None = None
    SourceAccessConfigurations: list[LambdaSourceAccessConfiguration] | None = None
    SelfManagedEventSource: LambdaSelfManagedEventSource | None = None
    FunctionResponseTypes: list[LambdaFunctionResponseType] | None = None
    AmazonManagedKafkaEventSourceConfig: LambdaAmazonManagedKafkaEventSourceConfig | None = None
    SelfManagedKafkaEventSourceConfig: LambdaSelfManagedKafkaEventSourceConfig | None = None
    DocumentDBEventSourceConfig: LambdaDocumentDBEventSourceConfig | None = None
    ProvisionedPollerConfig: LambdaProvisionedPollerConfig | None = None
