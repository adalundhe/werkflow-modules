from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_configuration_template_delivery_config_values import CloudWatchLogsConfigurationTemplateDeliveryConfigValues
from .cloud_watch_logs_delivery_source_configuration_schema import CloudWatchLogsDeliverySourceConfigurationSchema
from .cloud_watch_logs_record_field import CloudWatchLogsRecordField
from .cloud_watch_logs_s3_tables_integration import CloudWatchLogsS3TablesIntegration


class CloudWatchLogsConfigurationTemplate(BaseModel):
    service: StrictStr | None = None
    logType: StrictStr | None = None
    resourceType: StrictStr | None = None
    deliveryDestinationType: StrictStr | None = None
    defaultDeliveryConfigValues: CloudWatchLogsConfigurationTemplateDeliveryConfigValues | None = None
    allowedFields: list[CloudWatchLogsRecordField] | None = None
    allowedOutputFormats: list[StrictStr] | None = None
    allowedActionForAllowVendedLogsDeliveryForResource: StrictStr | None = None
    allowedFieldDelimiters: list[StrictStr] | None = None
    allowedSuffixPathFields: list[StrictStr] | None = None
    deliverySourceConfiguration: list[CloudWatchLogsDeliverySourceConfigurationSchema] | None = None
    s3TablesIntegration: CloudWatchLogsS3TablesIntegration | None = None
