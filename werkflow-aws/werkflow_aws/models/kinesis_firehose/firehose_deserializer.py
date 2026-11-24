from __future__ import annotations
from pydantic import BaseModel
from .firehose_hive_json_ser_de import FirehoseHiveJsonSerDe
from .firehose_open_x_json_ser_de import FirehoseOpenXJsonSerDe


class FirehoseDeserializer(BaseModel):
    OpenXJsonSerDe: FirehoseOpenXJsonSerDe | None = None
    HiveJsonSerDe: FirehoseHiveJsonSerDe | None = None
