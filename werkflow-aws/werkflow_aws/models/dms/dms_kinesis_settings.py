from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DMSKinesisSettings(BaseModel):
    StreamArn: StrictStr | None = None
    MessageFormat: StrictStr | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    IncludeTransactionDetails: StrictBool | None = None
    IncludePartitionValue: StrictBool | None = None
    PartitionIncludeSchemaTable: StrictBool | None = None
    IncludeTableAlterOperations: StrictBool | None = None
    IncludeControlDetails: StrictBool | None = None
    IncludeNullAndEmpty: StrictBool | None = None
    NoHexPrefix: StrictBool | None = None
    UseLargeIntegerValue: StrictBool | None = None
