from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_processor_parameter import FirehoseProcessorParameter


class FirehoseProcessor(BaseModel):
    Type: StrictStr | None = None
    Parameters: list[FirehoseProcessorParameter] | None = None
