from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .firehose_input_format_configuration import FirehoseInputFormatConfiguration
from .firehose_output_format_configuration import FirehoseOutputFormatConfiguration
from .firehose_schema_configuration import FirehoseSchemaConfiguration


class FirehoseDataFormatConversionConfiguration(BaseModel):
    SchemaConfiguration: FirehoseSchemaConfiguration | None = None
    InputFormatConfiguration: FirehoseInputFormatConfiguration | None = None
    OutputFormatConfiguration: FirehoseOutputFormatConfiguration | None = None
    Enabled: StrictBool | None = None
