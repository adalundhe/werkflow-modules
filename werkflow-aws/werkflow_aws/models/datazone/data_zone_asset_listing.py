from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_detailed_glossary_term import DataZoneDetailedGlossaryTerm
from .data_zone_time_series_data_point_summary_form_output import DataZoneTimeSeriesDataPointSummaryFormOutput


class DataZoneAssetListing(BaseModel):
    assetId: StrictStr | None = None
    assetRevision: StrictStr | None = None
    assetType: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    forms: StrictStr | None = None
    latestTimeSeriesDataPointForms: list[DataZoneTimeSeriesDataPointSummaryFormOutput] | None = None
    glossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None
    governedGlossaryTerms: list[DataZoneDetailedGlossaryTerm] | None = None
    owningProjectId: StrictStr | None = None
