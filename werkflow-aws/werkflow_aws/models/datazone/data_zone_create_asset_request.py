from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_form_input import DataZoneFormInput
from .data_zone_prediction_configuration import DataZonePredictionConfiguration


class DataZoneCreateAssetRequest(BaseModel):
    name: StrictStr
    domainIdentifier: StrictStr
    typeIdentifier: StrictStr
    owningProjectIdentifier: StrictStr
    externalIdentifier: StrictStr | None = None
    typeRevision: StrictStr | None = None
    description: StrictStr | None = None
    glossaryTerms: list[StrictStr] | None = None
    formsInput: list[DataZoneFormInput] | None = None
    predictionConfiguration: DataZonePredictionConfiguration | None = None
    clientToken: StrictStr | None = None
