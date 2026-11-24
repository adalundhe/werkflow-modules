from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_input_serialization import AWSS3InputSerialization
from .awss3_output_serialization import AWSS3OutputSerialization


class AWSS3SelectParameters(BaseModel):
    InputSerialization: AWSS3InputSerialization
    ExpressionType: Literal['SQL']
    Expression: StrictStr
    OutputSerialization: AWSS3OutputSerialization
