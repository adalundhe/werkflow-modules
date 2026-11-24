from __future__ import annotations
from pydantic import BaseModel
from .firehose_orc_ser_de import FirehoseOrcSerDe
from .firehose_parquet_ser_de import FirehoseParquetSerDe


class FirehoseSerializer(BaseModel):
    ParquetSerDe: FirehoseParquetSerDe | None = None
    OrcSerDe: FirehoseOrcSerDe | None = None
