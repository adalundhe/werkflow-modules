from __future__ import annotations
from pydantic import BaseModel
from .glue_aggregate import GlueAggregate
from .glue_amazon_redshift_source import GlueAmazonRedshiftSource
from .glue_amazon_redshift_target import GlueAmazonRedshiftTarget
from .glue_apply_mapping import GlueApplyMapping
from .glue_athena_connector_source import GlueAthenaConnectorSource
from .glue_basic_catalog_target import GlueBasicCatalogTarget
from .glue_catalog_delta_source import GlueCatalogDeltaSource
from .glue_catalog_hudi_source import GlueCatalogHudiSource
from .glue_catalog_iceberg_source import GlueCatalogIcebergSource
from .glue_catalog_kafka_source import GlueCatalogKafkaSource
from .glue_catalog_kinesis_source import GlueCatalogKinesisSource
from .glue_catalog_source import GlueCatalogSource
from .glue_connector_data_source import GlueConnectorDataSource
from .glue_connector_data_target import GlueConnectorDataTarget
from .glue_custom_code import GlueCustomCode
from .glue_direct_jdbc_source import GlueDirectJDBCSource
from .glue_direct_kafka_source import GlueDirectKafkaSource
from .glue_direct_kinesis_source import GlueDirectKinesisSource
from .glue_drop_duplicates import GlueDropDuplicates
from .glue_drop_fields import GlueDropFields
from .glue_drop_null_fields import GlueDropNullFields
from .glue_dynamic_transform import GlueDynamicTransform
from .glue_dynamo_db_catalog_source import GlueDynamoDBCatalogSource
from .glue_dynamo_dbelt_connector_source import GlueDynamoDBELTConnectorSource
from .glue_evaluate_data_quality import GlueEvaluateDataQuality
from .glue_evaluate_data_quality_multi_frame import GlueEvaluateDataQualityMultiFrame
from .glue_fill_missing_values import GlueFillMissingValues
from .glue_filter import GlueFilter
from .glue_governed_catalog_source import GlueGovernedCatalogSource
from .glue_governed_catalog_target import GlueGovernedCatalogTarget
from .glue_jdbc_connector_source import GlueJDBCConnectorSource
from .glue_jdbc_connector_target import GlueJDBCConnectorTarget
from .glue_join import GlueJoin
from .glue_merge import GlueMerge
from .glue_microsoft_sql_server_catalog_source import GlueMicrosoftSQLServerCatalogSource
from .glue_microsoft_sql_server_catalog_target import GlueMicrosoftSQLServerCatalogTarget
from .glue_my_sql_catalog_source import GlueMySQLCatalogSource
from .glue_my_sql_catalog_target import GlueMySQLCatalogTarget
from .glue_oracle_sql_catalog_source import GlueOracleSQLCatalogSource
from .glue_oracle_sql_catalog_target import GlueOracleSQLCatalogTarget
from .glue_pii_detection import GluePIIDetection
from .glue_postgre_sql_catalog_source import GluePostgreSQLCatalogSource
from .glue_postgre_sql_catalog_target import GluePostgreSQLCatalogTarget
from .glue_recipe import GlueRecipe
from .glue_redshift_source import GlueRedshiftSource
from .glue_redshift_target import GlueRedshiftTarget
from .glue_relational_catalog_source import GlueRelationalCatalogSource
from .glue_rename_field import GlueRenameField
from .glue_route import GlueRoute
from .glue_s3_catalog_delta_source import GlueS3CatalogDeltaSource
from .glue_s3_catalog_hudi_source import GlueS3CatalogHudiSource
from .glue_s3_catalog_iceberg_source import GlueS3CatalogIcebergSource
from .glue_s3_catalog_source import GlueS3CatalogSource
from .glue_s3_catalog_target import GlueS3CatalogTarget
from .glue_s3_csv_source import GlueS3CsvSource
from .glue_s3_delta_catalog_target import GlueS3DeltaCatalogTarget
from .glue_s3_delta_direct_target import GlueS3DeltaDirectTarget
from .glue_s3_delta_source import GlueS3DeltaSource
from .glue_s3_direct_target import GlueS3DirectTarget
from .glue_s3_excel_source import GlueS3ExcelSource
from .glue_s3_glue_parquet_target import GlueS3GlueParquetTarget
from .glue_s3_hudi_catalog_target import GlueS3HudiCatalogTarget
from .glue_s3_hudi_direct_target import GlueS3HudiDirectTarget
from .glue_s3_hudi_source import GlueS3HudiSource
from .glue_s3_hyper_direct_target import GlueS3HyperDirectTarget
from .glue_s3_iceberg_catalog_target import GlueS3IcebergCatalogTarget
from .glue_s3_iceberg_direct_target import GlueS3IcebergDirectTarget
from .glue_s3_json_source import GlueS3JsonSource
from .glue_s3_parquet_source import GlueS3ParquetSource
from .glue_select_fields import GlueSelectFields
from .glue_select_from_collection import GlueSelectFromCollection
from .glue_snowflake_source import GlueSnowflakeSource
from .glue_snowflake_target import GlueSnowflakeTarget
from .glue_spark_connector_source import GlueSparkConnectorSource
from .glue_spark_connector_target import GlueSparkConnectorTarget
from .glue_spark_sql import GlueSparkSQL
from .glue_spigot import GlueSpigot
from .glue_split_fields import GlueSplitFields
from .glue_union import GlueUnion


class GlueCodeGenConfigurationNode(BaseModel):
    AthenaConnectorSource: GlueAthenaConnectorSource | None = None
    JDBCConnectorSource: GlueJDBCConnectorSource | None = None
    SparkConnectorSource: GlueSparkConnectorSource | None = None
    CatalogSource: GlueCatalogSource | None = None
    RedshiftSource: GlueRedshiftSource | None = None
    S3CatalogSource: GlueS3CatalogSource | None = None
    S3CsvSource: GlueS3CsvSource | None = None
    S3JsonSource: GlueS3JsonSource | None = None
    S3ParquetSource: GlueS3ParquetSource | None = None
    RelationalCatalogSource: GlueRelationalCatalogSource | None = None
    DynamoDBCatalogSource: GlueDynamoDBCatalogSource | None = None
    JDBCConnectorTarget: GlueJDBCConnectorTarget | None = None
    SparkConnectorTarget: GlueSparkConnectorTarget | None = None
    CatalogTarget: GlueBasicCatalogTarget | None = None
    RedshiftTarget: GlueRedshiftTarget | None = None
    S3CatalogTarget: GlueS3CatalogTarget | None = None
    S3GlueParquetTarget: GlueS3GlueParquetTarget | None = None
    S3DirectTarget: GlueS3DirectTarget | None = None
    ApplyMapping: GlueApplyMapping | None = None
    SelectFields: GlueSelectFields | None = None
    DropFields: GlueDropFields | None = None
    RenameField: GlueRenameField | None = None
    Spigot: GlueSpigot | None = None
    Join: GlueJoin | None = None
    SplitFields: GlueSplitFields | None = None
    SelectFromCollection: GlueSelectFromCollection | None = None
    FillMissingValues: GlueFillMissingValues | None = None
    Filter: GlueFilter | None = None
    CustomCode: GlueCustomCode | None = None
    SparkSQL: GlueSparkSQL | None = None
    DirectKinesisSource: GlueDirectKinesisSource | None = None
    DirectKafkaSource: GlueDirectKafkaSource | None = None
    CatalogKinesisSource: GlueCatalogKinesisSource | None = None
    CatalogKafkaSource: GlueCatalogKafkaSource | None = None
    DropNullFields: GlueDropNullFields | None = None
    Merge: GlueMerge | None = None
    Union: GlueUnion | None = None
    PIIDetection: GluePIIDetection | None = None
    Aggregate: GlueAggregate | None = None
    DropDuplicates: GlueDropDuplicates | None = None
    GovernedCatalogTarget: GlueGovernedCatalogTarget | None = None
    GovernedCatalogSource: GlueGovernedCatalogSource | None = None
    MicrosoftSQLServerCatalogSource: GlueMicrosoftSQLServerCatalogSource | None = None
    MySQLCatalogSource: GlueMySQLCatalogSource | None = None
    OracleSQLCatalogSource: GlueOracleSQLCatalogSource | None = None
    PostgreSQLCatalogSource: GluePostgreSQLCatalogSource | None = None
    MicrosoftSQLServerCatalogTarget: GlueMicrosoftSQLServerCatalogTarget | None = None
    MySQLCatalogTarget: GlueMySQLCatalogTarget | None = None
    OracleSQLCatalogTarget: GlueOracleSQLCatalogTarget | None = None
    PostgreSQLCatalogTarget: GluePostgreSQLCatalogTarget | None = None
    Route: GlueRoute | None = None
    DynamicTransform: GlueDynamicTransform | None = None
    EvaluateDataQuality: GlueEvaluateDataQuality | None = None
    S3CatalogHudiSource: GlueS3CatalogHudiSource | None = None
    CatalogHudiSource: GlueCatalogHudiSource | None = None
    S3HudiSource: GlueS3HudiSource | None = None
    S3HudiCatalogTarget: GlueS3HudiCatalogTarget | None = None
    S3HudiDirectTarget: GlueS3HudiDirectTarget | None = None
    DirectJDBCSource: GlueDirectJDBCSource | None = None
    S3CatalogDeltaSource: GlueS3CatalogDeltaSource | None = None
    CatalogDeltaSource: GlueCatalogDeltaSource | None = None
    S3DeltaSource: GlueS3DeltaSource | None = None
    S3DeltaCatalogTarget: GlueS3DeltaCatalogTarget | None = None
    S3DeltaDirectTarget: GlueS3DeltaDirectTarget | None = None
    AmazonRedshiftSource: GlueAmazonRedshiftSource | None = None
    AmazonRedshiftTarget: GlueAmazonRedshiftTarget | None = None
    EvaluateDataQualityMultiFrame: GlueEvaluateDataQualityMultiFrame | None = None
    Recipe: GlueRecipe | None = None
    SnowflakeSource: GlueSnowflakeSource | None = None
    SnowflakeTarget: GlueSnowflakeTarget | None = None
    ConnectorDataSource: GlueConnectorDataSource | None = None
    ConnectorDataTarget: GlueConnectorDataTarget | None = None
    S3CatalogIcebergSource: GlueS3CatalogIcebergSource | None = None
    CatalogIcebergSource: GlueCatalogIcebergSource | None = None
    S3IcebergCatalogTarget: GlueS3IcebergCatalogTarget | None = None
    S3IcebergDirectTarget: GlueS3IcebergDirectTarget | None = None
    S3ExcelSource: GlueS3ExcelSource | None = None
    S3HyperDirectTarget: GlueS3HyperDirectTarget | None = None
    DynamoDBELTConnectorSource: GlueDynamoDBELTConnectorSource | None = None
