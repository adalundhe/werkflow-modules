from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_input_serialization_model import AWSS3InputSerializationModel
from .awss3_output_serialization_model import AWSS3OutputSerializationModel
from .awss3_request_progress import AWSS3RequestProgress
from .awss3_scan_range import AWSS3ScanRange


class AWSS3SelectObjectContentRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    Expression: StrictStr
    ExpressionType: Literal['SQL']
    InputSerialization: AWSS3InputSerializationModel
    OutputSerialization: AWSS3OutputSerializationModel
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    SSECustomerKeyMD5: StrictStr | None = None
    RequestProgress: AWSS3RequestProgress | None = None
    ScanRange: AWSS3ScanRange | None = None
    ExpectedBucketOwner: StrictStr | None = None
