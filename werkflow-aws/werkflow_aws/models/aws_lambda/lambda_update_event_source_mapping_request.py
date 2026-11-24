from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lambda_amazon_managed_kafka_event_source_config_model import LambdaAmazonManagedKafkaEventSourceConfigModel
from .lambda_destination_config_model import LambdaDestinationConfigModel
from .lambda_document_db_event_source_config_model import LambdaDocumentDBEventSourceConfigModel
from .lambda_event_source_mapping_logging_config_model import LambdaEventSourceMappingLoggingConfigModel
from .lambda_event_source_mapping_metrics_config_model import LambdaEventSourceMappingMetricsConfigModel
from .lambda_filter_criteria_model import LambdaFilterCriteriaModel
from .lambda_provisioned_poller_config_model import LambdaProvisionedPollerConfigModel
from .lambda_scaling_config_model import LambdaScalingConfigModel
from .lambda_self_managed_kafka_event_source_config_model import LambdaSelfManagedKafkaEventSourceConfigModel
from .lambda_source_access_configuration_model import LambdaSourceAccessConfigurationModel


class LambdaUpdateEventSourceMappingRequest(BaseModel):
    UUID: StrictStr
    FunctionName: StrictStr | None = None
    Enabled: StrictBool | None = None
    BatchSize: StrictInt | None = None
    FilterCriteria: LambdaFilterCriteriaModel | None = None
    KMSKeyArn: StrictStr | None = None
    MetricsConfig: LambdaEventSourceMappingMetricsConfigModel | None = None
    LoggingConfig: LambdaEventSourceMappingLoggingConfigModel | None = None
    ScalingConfig: LambdaScalingConfigModel | None = None
    MaximumBatchingWindowInSeconds: StrictInt | None = None
    ParallelizationFactor: StrictInt | None = None
    DestinationConfig: LambdaDestinationConfigModel | None = None
    MaximumRecordAgeInSeconds: StrictInt | None = None
    BisectBatchOnFunctionError: StrictBool | None = None
    MaximumRetryAttempts: StrictInt | None = None
    TumblingWindowInSeconds: StrictInt | None = None
    SourceAccessConfigurations: list[LambdaSourceAccessConfigurationModel] | None = None
    FunctionResponseTypes: list[Literal['ReportBatchItemFailures']] | None = None
    AmazonManagedKafkaEventSourceConfig: LambdaAmazonManagedKafkaEventSourceConfigModel | None = None
    SelfManagedKafkaEventSourceConfig: LambdaSelfManagedKafkaEventSourceConfigModel | None = None
    DocumentDBEventSourceConfig: LambdaDocumentDBEventSourceConfigModel | None = None
    ProvisionedPollerConfig: LambdaProvisionedPollerConfigModel | None = None
