from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_evaluation_metrics import GlueEvaluationMetrics
from .glue_schema_column import GlueSchemaColumn
from .glue_table import GlueTable
from .glue_transform_encryption import GlueTransformEncryption
from .glue_transform_parameters import GlueTransformParameters


class GlueGetMLTransformResponse(BaseModel):
    TransformId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    InputRecordTables: list[GlueTable] | None = None
    Parameters: GlueTransformParameters | None = None
    EvaluationMetrics: GlueEvaluationMetrics | None = None
    LabelCount: StrictInt | None = None
    Schema: list[GlueSchemaColumn] | None = None
    Role: StrictStr | None = None
    GlueVersion: StrictStr | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    WorkerType: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    Timeout: StrictInt | None = None
    MaxRetries: StrictInt | None = None
    TransformEncryption: GlueTransformEncryption | None = None
    ResponseMetadata: dict[str, Any] | None = None
