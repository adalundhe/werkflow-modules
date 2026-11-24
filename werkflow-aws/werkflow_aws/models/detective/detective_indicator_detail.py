from __future__ import annotations
from pydantic import BaseModel
from .detective_flagged_ip_address_detail import DetectiveFlaggedIpAddressDetail
from .detective_impossible_travel_detail import DetectiveImpossibleTravelDetail
from .detective_new_aso_detail import DetectiveNewAsoDetail
from .detective_new_geolocation_detail import DetectiveNewGeolocationDetail
from .detective_new_user_agent_detail import DetectiveNewUserAgentDetail
from .detective_related_finding_detail import DetectiveRelatedFindingDetail
from .detective_related_finding_group_detail import DetectiveRelatedFindingGroupDetail
from .detective_tt_ps_observed_detail import DetectiveTTPsObservedDetail


class DetectiveIndicatorDetail(BaseModel):
    TTPsObservedDetail: DetectiveTTPsObservedDetail | None = None
    ImpossibleTravelDetail: DetectiveImpossibleTravelDetail | None = None
    FlaggedIpAddressDetail: DetectiveFlaggedIpAddressDetail | None = None
    NewGeolocationDetail: DetectiveNewGeolocationDetail | None = None
    NewAsoDetail: DetectiveNewAsoDetail | None = None
    NewUserAgentDetail: DetectiveNewUserAgentDetail | None = None
    RelatedFindingDetail: DetectiveRelatedFindingDetail | None = None
    RelatedFindingGroupDetail: DetectiveRelatedFindingGroupDetail | None = None
