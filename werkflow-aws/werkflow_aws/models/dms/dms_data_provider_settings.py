from __future__ import annotations
from pydantic import BaseModel
from .dms_doc_db_data_provider_settings import DMSDocDbDataProviderSettings
from .dms_ibm_db2_luw_data_provider_settings import DMSIbmDb2LuwDataProviderSettings
from .dms_ibm_db2z_os_data_provider_settings import DMSIbmDb2zOsDataProviderSettings
from .dms_maria_db_data_provider_settings import DMSMariaDbDataProviderSettings
from .dms_microsoft_sql_server_data_provider_settings import DMSMicrosoftSqlServerDataProviderSettings
from .dms_mongo_db_data_provider_settings import DMSMongoDbDataProviderSettings
from .dms_my_sql_data_provider_settings import DMSMySqlDataProviderSettings
from .dms_oracle_data_provider_settings import DMSOracleDataProviderSettings
from .dms_postgre_sql_data_provider_settings import DMSPostgreSqlDataProviderSettings
from .dms_redshift_data_provider_settings import DMSRedshiftDataProviderSettings
from .dms_sybase_ase_data_provider_settings import DMSSybaseAseDataProviderSettings


class DMSDataProviderSettings(BaseModel):
    RedshiftSettings: DMSRedshiftDataProviderSettings | None = None
    PostgreSqlSettings: DMSPostgreSqlDataProviderSettings | None = None
    MySqlSettings: DMSMySqlDataProviderSettings | None = None
    OracleSettings: DMSOracleDataProviderSettings | None = None
    SybaseAseSettings: DMSSybaseAseDataProviderSettings | None = None
    MicrosoftSqlServerSettings: DMSMicrosoftSqlServerDataProviderSettings | None = None
    DocDbSettings: DMSDocDbDataProviderSettings | None = None
    MariaDbSettings: DMSMariaDbDataProviderSettings | None = None
    IbmDb2LuwSettings: DMSIbmDb2LuwDataProviderSettings | None = None
    IbmDb2zOsSettings: DMSIbmDb2zOsDataProviderSettings | None = None
    MongoDbSettings: DMSMongoDbDataProviderSettings | None = None
