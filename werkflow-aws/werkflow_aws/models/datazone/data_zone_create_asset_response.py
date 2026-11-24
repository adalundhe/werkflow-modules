from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_asset_listing_details import DataZoneAssetListingDetails
from .data_zone_form_output import DataZoneFormOutput
from .data_zone_prediction_configuration import DataZonePredictionConfiguration
from .data_zone_time_series_data_point_summary_form_output import DataZoneTimeSeriesDataPointSummaryFormOutput


class DataZoneCreateAssetResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    typeIdentifier: StrictStr | None = None
    typeRevision: StrictStr | None = None
    externalIdentifier: StrictStr | None = None
    revision: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    firstRevisionCreatedAt: datetime.datetime | StrictStr | None = None
    firstRevisionCreatedBy: StrictStr | None = None
    glossaryTerms: list[StrictStr] | None = None
    governedGlossaryTerms: list[StrictStr] | None = None
    owningProjectId: StrictStr | None = None
    domainId: StrictStr | None = None
    listing: DataZoneAssetListingDetails | None = None
    formsOutput: list[DataZoneFormOutput] | None = None
    readOnlyFormsOutput: list[DataZoneFormOutput] | None = None
    latestTimeSeriesDataPointFormsOutput: list[DataZoneTimeSeriesDataPointSummaryFormOutput] | None = None
    predictionConfiguration: DataZonePredictionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
