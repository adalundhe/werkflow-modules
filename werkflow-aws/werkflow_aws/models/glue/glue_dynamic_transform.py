from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema
from .glue_transform_config_parameter import GlueTransformConfigParameter


class GlueDynamicTransform(BaseModel):
    Name: StrictStr | None = None
    TransformName: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Parameters: list[GlueTransformConfigParameter] | None = None
    FunctionName: StrictStr | None = None
    Path: StrictStr | None = None
    Version: StrictStr | None = None
    OutputSchemas: list[GlueSchema] | None = None
