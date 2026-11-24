from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_amazon_elasticsearch_parameters import QuickSightAmazonElasticsearchParameters
from .quick_sight_amazon_open_search_parameters import QuickSightAmazonOpenSearchParameters
from .quick_sight_athena_parameters import QuickSightAthenaParameters
from .quick_sight_aurora_parameters import QuickSightAuroraParameters
from .quick_sight_aurora_postgre_sql_parameters import QuickSightAuroraPostgreSqlParameters
from .quick_sight_aws_iot_analytics_parameters import QuickSightAwsIotAnalyticsParameters
from .quick_sight_big_query_parameters import QuickSightBigQueryParameters
from .quick_sight_confluence_parameters import QuickSightConfluenceParameters
from .quick_sight_custom_connection_parameters import QuickSightCustomConnectionParameters
from .quick_sight_databricks_parameters import QuickSightDatabricksParameters
from .quick_sight_exasol_parameters import QuickSightExasolParameters
from .quick_sight_fmkb_parameters import QuickSightFMKBParameters
from .quick_sight_google_drive_parameters import QuickSightGoogleDriveParameters
from .quick_sight_impala_parameters import QuickSightImpalaParameters
from .quick_sight_jira_parameters import QuickSightJiraParameters
from .quick_sight_maria_db_parameters import QuickSightMariaDbParameters
from .quick_sight_my_sql_parameters import QuickSightMySqlParameters
from .quick_sight_one_drive_parameters import QuickSightOneDriveParameters
from .quick_sight_oracle_parameters import QuickSightOracleParameters
from .quick_sight_postgre_sql_parameters import QuickSightPostgreSqlParameters
from .quick_sight_presto_parameters import QuickSightPrestoParameters
from .quick_sight_q_business_parameters import QuickSightQBusinessParameters
from .quick_sight_rds_parameters import QuickSightRdsParameters
from .quick_sight_redshift_parameters import QuickSightRedshiftParameters
from .quick_sight_s3_knowledge_base_parameters import QuickSightS3KnowledgeBaseParameters
from .quick_sight_s3_parameters import QuickSightS3Parameters
from .quick_sight_s3_tables_parameters import QuickSightS3TablesParameters
from .quick_sight_service_now_parameters import QuickSightServiceNowParameters
from .quick_sight_share_point_parameters import QuickSightSharePointParameters
from .quick_sight_snowflake_parameters import QuickSightSnowflakeParameters
from .quick_sight_spark_parameters import QuickSightSparkParameters
from .quick_sight_sql_server_parameters import QuickSightSqlServerParameters
from .quick_sight_starburst_parameters import QuickSightStarburstParameters
from .quick_sight_teradata_parameters import QuickSightTeradataParameters
from .quick_sight_trino_parameters import QuickSightTrinoParameters
from .quick_sight_twitter_parameters import QuickSightTwitterParameters
from .quick_sight_web_crawler_parameters import QuickSightWebCrawlerParameters


class QuickSightDataSourceParameters(BaseModel):
    AmazonElasticsearchParameters: QuickSightAmazonElasticsearchParameters | None = None
    AthenaParameters: QuickSightAthenaParameters | None = None
    AuroraParameters: QuickSightAuroraParameters | None = None
    AuroraPostgreSqlParameters: QuickSightAuroraPostgreSqlParameters | None = None
    AwsIotAnalyticsParameters: QuickSightAwsIotAnalyticsParameters | None = None
    JiraParameters: QuickSightJiraParameters | None = None
    MariaDbParameters: QuickSightMariaDbParameters | None = None
    MySqlParameters: QuickSightMySqlParameters | None = None
    OracleParameters: QuickSightOracleParameters | None = None
    PostgreSqlParameters: QuickSightPostgreSqlParameters | None = None
    PrestoParameters: QuickSightPrestoParameters | None = None
    RdsParameters: QuickSightRdsParameters | None = None
    RedshiftParameters: QuickSightRedshiftParameters | None = None
    S3Parameters: QuickSightS3Parameters | None = None
    S3TablesParameters: QuickSightS3TablesParameters | None = None
    S3KnowledgeBaseParameters: QuickSightS3KnowledgeBaseParameters | None = None
    ServiceNowParameters: QuickSightServiceNowParameters | None = None
    SnowflakeParameters: QuickSightSnowflakeParameters | None = None
    SparkParameters: QuickSightSparkParameters | None = None
    SqlServerParameters: QuickSightSqlServerParameters | None = None
    TeradataParameters: QuickSightTeradataParameters | None = None
    TwitterParameters: QuickSightTwitterParameters | None = None
    AmazonOpenSearchParameters: QuickSightAmazonOpenSearchParameters | None = None
    ExasolParameters: QuickSightExasolParameters | None = None
    DatabricksParameters: QuickSightDatabricksParameters | None = None
    StarburstParameters: QuickSightStarburstParameters | None = None
    TrinoParameters: QuickSightTrinoParameters | None = None
    BigQueryParameters: QuickSightBigQueryParameters | None = None
    ImpalaParameters: QuickSightImpalaParameters | None = None
    CustomConnectionParameters: QuickSightCustomConnectionParameters | None = None
    WebCrawlerParameters: QuickSightWebCrawlerParameters | None = None
    ConfluenceParameters: QuickSightConfluenceParameters | None = None
    QBusinessParameters: QuickSightQBusinessParameters | None = None
    SharePointParameters: QuickSightSharePointParameters | None = None
    GoogleDriveParameters: QuickSightGoogleDriveParameters | None = None
    OneDriveParameters: QuickSightOneDriveParameters | None = None
    FMKBParameters: QuickSightFMKBParameters | None = None
