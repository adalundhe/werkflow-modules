from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowRedshiftConnectorProfileProperties(BaseModel):
    databaseUrl: StrictStr | None = None
    bucketName: StrictStr | None = None
    bucketPrefix: StrictStr | None = None
    roleArn: StrictStr | None = None
    dataApiRoleArn: StrictStr | None = None
    isRedshiftServerless: StrictBool | None = None
    clusterIdentifier: StrictStr | None = None
    workgroupName: StrictStr | None = None
    databaseName: StrictStr | None = None
