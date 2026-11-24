from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .athena_customer_content_encryption_configuration import AthenaCustomerContentEncryptionConfiguration
from .athena_engine_configuration_model import AthenaEngineConfigurationModel
from .athena_engine_version_model import AthenaEngineVersionModel
from .athena_identity_center_configuration import AthenaIdentityCenterConfiguration
from .athena_managed_query_results_configuration_model import AthenaManagedQueryResultsConfigurationModel
from .athena_monitoring_configuration import AthenaMonitoringConfiguration
from .athena_query_results_s3_access_grants_configuration_model import AthenaQueryResultsS3AccessGrantsConfigurationModel
from .athena_result_configuration_model import AthenaResultConfigurationModel
from .athena_system_table_status import AthenaSystemTableStatus


class AthenaWorkGroupConfiguration(BaseModel):
    ResultConfiguration: AthenaResultConfigurationModel | None = None
    ManagedQueryResultsConfiguration: AthenaManagedQueryResultsConfigurationModel | None = None
    EnforceWorkGroupConfiguration: StrictBool | None = None
    PublishCloudWatchMetricsEnabled: StrictBool | None = None
    BytesScannedCutoffPerQuery: StrictInt | None = None
    RequesterPaysEnabled: StrictBool | None = None
    EngineVersion: AthenaEngineVersionModel | None = None
    AdditionalConfiguration: StrictStr | None = None
    ExecutionRole: StrictStr | None = None
    MonitoringConfiguration: AthenaMonitoringConfiguration | None = None
    EngineConfiguration: AthenaEngineConfigurationModel | None = None
    CustomerContentEncryptionConfiguration: AthenaCustomerContentEncryptionConfiguration | None = None
    EnableMinimumEncryptionConfiguration: StrictBool | None = None
    IdentityCenterConfiguration: AthenaIdentityCenterConfiguration | None = None
    QueryResultsS3AccessGrantsConfiguration: AthenaQueryResultsS3AccessGrantsConfigurationModel | None = None
    SystemTableStatuses: list[AthenaSystemTableStatus] | None = None
