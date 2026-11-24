from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class AppSyncRdsHttpEndpointConfig(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    awsRegion: StrictStr | None = None
    dbClusterIdentifier: StrictStr | None = None
    databaseName: StrictStr | None = None
    schema_: StrictStr | None = Field(default=None, alias='schema')
    awsSecretStoreArn: StrictStr | None = None
