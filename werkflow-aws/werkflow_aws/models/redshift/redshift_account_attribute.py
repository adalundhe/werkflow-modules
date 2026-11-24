from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_attribute_value_target import RedshiftAttributeValueTarget


class RedshiftAccountAttribute(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeValues: list[RedshiftAttributeValueTarget] | None = None
