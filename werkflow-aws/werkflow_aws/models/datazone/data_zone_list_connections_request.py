from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListConnectionsRequest(BaseModel):
    domainIdentifier: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: Literal['NAME'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    name: StrictStr | None = None
    environmentIdentifier: StrictStr | None = None
    projectIdentifier: StrictStr | None = None
    type: Literal['ATHENA', 'BIGQUERY', 'DATABRICKS', 'DOCUMENTDB', 'DYNAMODB', 'HYPERPOD', 'IAM', 'MYSQL', 'OPENSEARCH', 'ORACLE', 'POSTGRESQL', 'REDSHIFT', 'S3', 'SAPHANA', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'TERADATA', 'VERTICA', 'WORKFLOWS_MWAA', 'AMAZON_Q', 'MLFLOW', 'VPC', 'GIT', 'ICEBERGRESTCATALOG', 'SNOWFLAKEICEBERGRESTCATALOG', 'DATABRICKSICEBERGRESTCATALOG', 'WORKDAYICEBERGRESTCATALOG', 'WORKDAYLDQ'] | None = None
    scope: Literal['DOMAIN', 'PROJECT'] | None = None
