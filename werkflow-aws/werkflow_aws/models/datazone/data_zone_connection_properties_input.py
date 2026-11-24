from __future__ import annotations
from pydantic import BaseModel
from .data_zone_amazon_q_properties_input import DataZoneAmazonQPropertiesInput
from .data_zone_athena_properties_input import DataZoneAthenaPropertiesInput
from .data_zone_git_properties_input import DataZoneGitPropertiesInput
from .data_zone_glue_properties_input import DataZoneGluePropertiesInput
from .data_zone_hyper_pod_properties_input import DataZoneHyperPodPropertiesInput
from .data_zone_iam_properties_input import DataZoneIamPropertiesInput
from .data_zone_lakehouse_properties_input import DataZoneLakehousePropertiesInput
from .data_zone_mlflow_properties_input import DataZoneMlflowPropertiesInput
from .data_zone_redshift_properties_input import DataZoneRedshiftPropertiesInput
from .data_zone_s3_properties_input import DataZoneS3PropertiesInput
from .data_zone_snowflake_properties_input import DataZoneSnowflakePropertiesInput
from .data_zone_spark_emr_properties_input import DataZoneSparkEmrPropertiesInput
from .data_zone_spark_glue_properties_input import DataZoneSparkGluePropertiesInput
from .data_zone_vpc_properties_input import DataZoneVpcPropertiesInput
from .data_zone_workflows_mwaa_properties_input import DataZoneWorkflowsMwaaPropertiesInput
from .data_zone_workflows_serverless_properties_input import DataZoneWorkflowsServerlessPropertiesInput


class DataZoneConnectionPropertiesInput(BaseModel):
    athenaProperties: DataZoneAthenaPropertiesInput | None = None
    glueProperties: DataZoneGluePropertiesInput | None = None
    hyperPodProperties: DataZoneHyperPodPropertiesInput | None = None
    iamProperties: DataZoneIamPropertiesInput | None = None
    redshiftProperties: DataZoneRedshiftPropertiesInput | None = None
    sparkEmrProperties: DataZoneSparkEmrPropertiesInput | None = None
    sparkGlueProperties: DataZoneSparkGluePropertiesInput | None = None
    s3Properties: DataZoneS3PropertiesInput | None = None
    snowflakeProperties: DataZoneSnowflakePropertiesInput | None = None
    amazonQProperties: DataZoneAmazonQPropertiesInput | None = None
    mlflowProperties: DataZoneMlflowPropertiesInput | None = None
    workflowsMwaaProperties: DataZoneWorkflowsMwaaPropertiesInput | None = None
    workflowsServerlessProperties: DataZoneWorkflowsServerlessPropertiesInput | None = None
    lakehouseProperties: DataZoneLakehousePropertiesInput | None = None
    vpcProperties: DataZoneVpcPropertiesInput | None = None
    gitProperties: DataZoneGitPropertiesInput | None = None
