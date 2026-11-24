from __future__ import annotations
from pydantic import BaseModel
from .data_zone_amazon_q_properties_output import DataZoneAmazonQPropertiesOutput
from .data_zone_athena_properties_output import DataZoneAthenaPropertiesOutput
from .data_zone_git_properties_output import DataZoneGitPropertiesOutput
from .data_zone_glue_properties_output import DataZoneGluePropertiesOutput
from .data_zone_hyper_pod_properties_output import DataZoneHyperPodPropertiesOutput
from .data_zone_iam_properties_output import DataZoneIamPropertiesOutput
from .data_zone_lakehouse_properties_output import DataZoneLakehousePropertiesOutput
from .data_zone_mlflow_properties_output import DataZoneMlflowPropertiesOutput
from .data_zone_redshift_properties_output import DataZoneRedshiftPropertiesOutput
from .data_zone_s3_properties_output import DataZoneS3PropertiesOutput
from .data_zone_snowflake_properties_output import DataZoneSnowflakePropertiesOutput
from .data_zone_spark_emr_properties_output import DataZoneSparkEmrPropertiesOutput
from .data_zone_spark_glue_properties_output import DataZoneSparkGluePropertiesOutput
from .data_zone_vpc_properties_output import DataZoneVpcPropertiesOutput
from .data_zone_workflows_mwaa_properties_output import DataZoneWorkflowsMwaaPropertiesOutput
from .data_zone_workflows_serverless_properties_output import DataZoneWorkflowsServerlessPropertiesOutput


class DataZoneConnectionPropertiesOutput(BaseModel):
    athenaProperties: DataZoneAthenaPropertiesOutput | None = None
    glueProperties: DataZoneGluePropertiesOutput | None = None
    hyperPodProperties: DataZoneHyperPodPropertiesOutput | None = None
    iamProperties: DataZoneIamPropertiesOutput | None = None
    redshiftProperties: DataZoneRedshiftPropertiesOutput | None = None
    sparkEmrProperties: DataZoneSparkEmrPropertiesOutput | None = None
    sparkGlueProperties: DataZoneSparkGluePropertiesOutput | None = None
    s3Properties: DataZoneS3PropertiesOutput | None = None
    snowflakeProperties: DataZoneSnowflakePropertiesOutput | None = None
    amazonQProperties: DataZoneAmazonQPropertiesOutput | None = None
    mlflowProperties: DataZoneMlflowPropertiesOutput | None = None
    workflowsMwaaProperties: DataZoneWorkflowsMwaaPropertiesOutput | None = None
    workflowsServerlessProperties: DataZoneWorkflowsServerlessPropertiesOutput | None = None
    lakehouseProperties: DataZoneLakehousePropertiesOutput | None = None
    vpcProperties: DataZoneVpcPropertiesOutput | None = None
    gitProperties: DataZoneGitPropertiesOutput | None = None
