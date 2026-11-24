from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .athena_customer_content_encryption_configuration import AthenaCustomerContentEncryptionConfiguration
from .athena_engine_configuration_model import AthenaEngineConfigurationModel
from .athena_engine_version_model import AthenaEngineVersionModel
from .athena_managed_query_results_configuration_updates import AthenaManagedQueryResultsConfigurationUpdates
from .athena_monitoring_configuration import AthenaMonitoringConfiguration
from .athena_query_results_s3_access_grants_configuration_model import AthenaQueryResultsS3AccessGrantsConfigurationModel
from .athena_result_configuration_updates import AthenaResultConfigurationUpdates


class AthenaWorkGroupConfigurationUpdates(BaseModel):
    EnforceWorkGroupConfiguration: StrictBool | None = None
    ResultConfigurationUpdates: AthenaResultConfigurationUpdates | None = None
    ManagedQueryResultsConfigurationUpdates: AthenaManagedQueryResultsConfigurationUpdates | None = None
    PublishCloudWatchMetricsEnabled: StrictBool | None = None
    BytesScannedCutoffPerQuery: StrictInt | None = None
    RemoveBytesScannedCutoffPerQuery: StrictBool | None = None
    RequesterPaysEnabled: StrictBool | None = None
    EngineVersion: AthenaEngineVersionModel | None = None
    RemoveCustomerContentEncryptionConfiguration: StrictBool | None = None
    AdditionalConfiguration: StrictStr | None = None
    ExecutionRole: StrictStr | None = None
    CustomerContentEncryptionConfiguration: AthenaCustomerContentEncryptionConfiguration | None = None
    EnableMinimumEncryptionConfiguration: StrictBool | None = None
    QueryResultsS3AccessGrantsConfiguration: AthenaQueryResultsS3AccessGrantsConfigurationModel | None = None
    MonitoringConfiguration: AthenaMonitoringConfiguration | None = None
    EngineConfiguration: AthenaEngineConfigurationModel | None = None
