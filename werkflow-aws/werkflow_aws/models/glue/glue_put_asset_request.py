from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_asset_form_input import GlueAssetFormInput


class GluePutAssetRequest(BaseModel):
    Identifier: StrictStr
    Name: StrictStr
    Forms: dict[StrictStr, GlueAssetFormInput]
    AssetTypeIdentifier: StrictStr | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
