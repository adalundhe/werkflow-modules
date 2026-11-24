from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dms_doc_db_settings import DMSDocDbSettings
from .dms_dynamo_db_settings import DMSDynamoDbSettings
from .dms_elasticsearch_settings import DMSElasticsearchSettings
from .dms_gcp_my_sql_settings import DMSGcpMySQLSettings
from .dmsibm_db2_settings import DMSIBMDb2Settings
from .dms_kafka_settings import DMSKafkaSettings
from .dms_kinesis_settings import DMSKinesisSettings
from .dms_lakehouse_settings import DMSLakehouseSettings
from .dms_microsoft_sql_server_settings import DMSMicrosoftSQLServerSettings
from .dms_mongo_db_settings import DMSMongoDbSettings
from .dms_my_sql_settings import DMSMySQLSettings
from .dms_neptune_settings import DMSNeptuneSettings
from .dms_oracle_settings import DMSOracleSettings
from .dms_postgre_sql_settings import DMSPostgreSQLSettings
from .dms_redis_settings import DMSRedisSettings
from .dms_redshift_settings import DMSRedshiftSettings
from .dmss3_settings import DMSS3Settings
from .dms_sybase_settings import DMSSybaseSettings
from .dms_timestream_settings import DMSTimestreamSettings
from .dms_transfer_settings import DmsTransferSettings as _DmsTransferSettingsType


class DMSEndpoint(BaseModel):
    EndpointIdentifier: StrictStr | None = None
    EndpointType: StrictStr | None = None
    EngineName: StrictStr | None = None
    EngineDisplayName: StrictStr | None = None
    Username: StrictStr | None = None
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    ExtraConnectionAttributes: StrictStr | None = None
    Status: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    SslMode: StrictStr | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    ExternalTableDefinition: StrictStr | None = None
    ExternalId: StrictStr | None = None
    IsReadOnly: StrictBool | None = None
    DynamoDbSettings: DMSDynamoDbSettings | None = None
    S3Settings: DMSS3Settings | None = None
    DmsTransferSettings: _DmsTransferSettingsType | None = None
    MongoDbSettings: DMSMongoDbSettings | None = None
    KinesisSettings: DMSKinesisSettings | None = None
    KafkaSettings: DMSKafkaSettings | None = None
    ElasticsearchSettings: DMSElasticsearchSettings | None = None
    NeptuneSettings: DMSNeptuneSettings | None = None
    RedshiftSettings: DMSRedshiftSettings | None = None
    PostgreSQLSettings: DMSPostgreSQLSettings | None = None
    MySQLSettings: DMSMySQLSettings | None = None
    OracleSettings: DMSOracleSettings | None = None
    SybaseSettings: DMSSybaseSettings | None = None
    MicrosoftSQLServerSettings: DMSMicrosoftSQLServerSettings | None = None
    IBMDb2Settings: DMSIBMDb2Settings | None = None
    DocDbSettings: DMSDocDbSettings | None = None
    RedisSettings: DMSRedisSettings | None = None
    GcpMySQLSettings: DMSGcpMySQLSettings | None = None
    TimestreamSettings: DMSTimestreamSettings | None = None
    LakehouseSettings: DMSLakehouseSettings | None = None
