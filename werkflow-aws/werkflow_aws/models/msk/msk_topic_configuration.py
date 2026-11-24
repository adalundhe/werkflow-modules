from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_record_converter import MSKRecordConverter
from .msk_record_schema import MSKRecordSchema


class MSKTopicConfiguration(BaseModel):
    RecordConverter: MSKRecordConverter | None = None
    RecordSchema: MSKRecordSchema | None = None
    TopicArn: StrictStr | None = None
