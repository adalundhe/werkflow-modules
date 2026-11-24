from __future__ import annotations
from pydantic import BaseModel
from .data_zone_amazon_q_properties_patch import DataZoneAmazonQPropertiesPatch
from .data_zone_athena_properties_patch import DataZoneAthenaPropertiesPatch
from .data_zone_git_properties_patch import DataZoneGitPropertiesPatch
from .data_zone_glue_properties_patch import DataZoneGluePropertiesPatch
from .data_zone_iam_properties_patch import DataZoneIamPropertiesPatch
from .data_zone_lakehouse_properties_patch import DataZoneLakehousePropertiesPatch
from .data_zone_mlflow_properties_patch import DataZoneMlflowPropertiesPatch
from .data_zone_redshift_properties_patch import DataZoneRedshiftPropertiesPatch
from .data_zone_s3_properties_patch import DataZoneS3PropertiesPatch
from .data_zone_snowflake_properties_patch import DataZoneSnowflakePropertiesPatch
from .data_zone_spark_emr_properties_patch import DataZoneSparkEmrPropertiesPatch
from .data_zone_vpc_properties_patch import DataZoneVpcPropertiesPatch


class DataZoneConnectionPropertiesPatch(BaseModel):
    athenaProperties: DataZoneAthenaPropertiesPatch | None = None
    glueProperties: DataZoneGluePropertiesPatch | None = None
    iamProperties: DataZoneIamPropertiesPatch | None = None
    redshiftProperties: DataZoneRedshiftPropertiesPatch | None = None
    sparkEmrProperties: DataZoneSparkEmrPropertiesPatch | None = None
    s3Properties: DataZoneS3PropertiesPatch | None = None
    snowflakeProperties: DataZoneSnowflakePropertiesPatch | None = None
    amazonQProperties: DataZoneAmazonQPropertiesPatch | None = None
    mlflowProperties: DataZoneMlflowPropertiesPatch | None = None
    lakehouseProperties: DataZoneLakehousePropertiesPatch | None = None
    vpcProperties: DataZoneVpcPropertiesPatch | None = None
    gitProperties: DataZoneGitPropertiesPatch | None = None
