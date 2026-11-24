from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_authentication_configuration_input import DataZoneAuthenticationConfigurationInput
from .data_zone_physical_connection_requirements import DataZonePhysicalConnectionRequirements


class DataZoneGlueConnectionInput(BaseModel):
    connectionProperties: dict[StrictStr, StrictStr] | None = None
    physicalConnectionRequirements: DataZonePhysicalConnectionRequirements | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    connectionType: Literal['SNOWFLAKE', 'BIGQUERY', 'DOCUMENTDB', 'DYNAMODB', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'SAPHANA', 'SQLSERVER', 'TERADATA', 'VERTICA', 'ICEBERGRESTCATALOG', 'SNOWFLAKEICEBERGRESTCATALOG', 'DATABRICKSICEBERGRESTCATALOG', 'WORKDAYICEBERGRESTCATALOG', 'WORKDAYLDQ'] | None = None
    matchCriteria: StrictStr | None = None
    validateCredentials: StrictBool | None = None
    validateForComputeEnvironments: list[Literal['SPARK', 'ATHENA', 'PYTHON']] | None = None
    sparkProperties: dict[StrictStr, StrictStr] | None = None
    athenaProperties: dict[StrictStr, StrictStr] | None = None
    pythonProperties: dict[StrictStr, StrictStr] | None = None
    authenticationConfiguration: DataZoneAuthenticationConfigurationInput | None = None
