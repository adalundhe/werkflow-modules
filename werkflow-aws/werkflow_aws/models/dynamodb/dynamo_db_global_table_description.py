from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dynamo_db_replica_description_model import DynamoDBReplicaDescriptionModel


class DynamoDBGlobalTableDescription(BaseModel):
    ReplicationGroup: list[DynamoDBReplicaDescriptionModel] | None = None
    GlobalTableArn: StrictStr | None = None
    CreationDateTime: datetime.datetime | StrictStr | None = None
    GlobalTableStatus: StrictStr | None = None
    GlobalTableName: StrictStr | None = None
