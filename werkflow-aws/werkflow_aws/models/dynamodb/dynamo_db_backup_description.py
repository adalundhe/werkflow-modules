from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_backup_details import DynamoDBBackupDetails
from .dynamo_db_source_table_details import DynamoDBSourceTableDetails
from .dynamo_db_source_table_feature_details import DynamoDBSourceTableFeatureDetails


class DynamoDBBackupDescription(BaseModel):
    BackupDetails: DynamoDBBackupDetails | None = None
    SourceTableDetails: DynamoDBSourceTableDetails | None = None
    SourceTableFeatureDetails: DynamoDBSourceTableFeatureDetails | None = None
