from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_input_serialization import GlacierInputSerialization
from .glacier_output_serialization import GlacierOutputSerialization


class GlacierSelectParameters(BaseModel):
    InputSerialization: GlacierInputSerialization | None = None
    ExpressionType: StrictStr | None = None
    Expression: StrictStr | None = None
    OutputSerialization: GlacierOutputSerialization | None = None
