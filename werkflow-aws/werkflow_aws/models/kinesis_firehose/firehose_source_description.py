from __future__ import annotations
from pydantic import BaseModel
from .firehose_database_source_description import FirehoseDatabaseSourceDescription
from .firehose_direct_put_source_description import FirehoseDirectPutSourceDescription
from .firehose_kinesis_stream_source_description import FirehoseKinesisStreamSourceDescription
from .firehose_msk_source_description import FirehoseMSKSourceDescription


class FirehoseSourceDescription(BaseModel):
    DirectPutSourceDescription: FirehoseDirectPutSourceDescription | None = None
    KinesisStreamSourceDescription: FirehoseKinesisStreamSourceDescription | None = None
    MSKSourceDescription: FirehoseMSKSourceDescription | None = None
    DatabaseSourceDescription: FirehoseDatabaseSourceDescription | None = None
