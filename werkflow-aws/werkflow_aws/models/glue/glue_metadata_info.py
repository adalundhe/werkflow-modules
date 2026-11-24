from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_other_metadata_value_list_item import GlueOtherMetadataValueListItem


class GlueMetadataInfo(BaseModel):
    MetadataValue: StrictStr | None = None
    CreatedTime: StrictStr | None = None
    OtherMetadataValueList: list[GlueOtherMetadataValueListItem] | None = None
