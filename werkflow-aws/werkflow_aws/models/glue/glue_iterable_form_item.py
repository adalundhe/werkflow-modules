from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_asset_form_entry import GlueAssetFormEntry


class GlueIterableFormItem(BaseModel):
    ItemId: StrictStr | None = None
    ItemName: StrictStr | None = None
    GlossaryTerms: list[StrictStr] | None = None
    Forms: dict[StrictStr, GlueAssetFormEntry] | None = None
    Attachments: dict[StrictStr, GlueAssetFormEntry] | None = None
