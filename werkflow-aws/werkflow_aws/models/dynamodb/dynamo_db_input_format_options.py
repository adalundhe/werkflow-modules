from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_csv_options import DynamoDBCsvOptions


class DynamoDBInputFormatOptions(BaseModel):
    Csv: DynamoDBCsvOptions | None = None
