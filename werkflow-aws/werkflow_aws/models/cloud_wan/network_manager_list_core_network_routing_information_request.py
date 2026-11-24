from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListCoreNetworkRoutingInformationRequest(BaseModel):
    CoreNetworkId: StrictStr
    SegmentName: StrictStr
    EdgeLocation: StrictStr
    NextHopFilters: dict[StrictStr, list[StrictStr]] | None = None
    ExactPrefixMatches: list[StrictStr] | None = None
    LongestPrefixMatches: list[StrictStr] | None = None
    SubnetOfMatches: list[StrictStr] | None = None
    SupernetOfMatches: list[StrictStr] | None = None
    LocalPreferenceMatches: list[StrictStr] | None = None
    ExactAsPathMatches: list[StrictStr] | None = None
    MedMatches: list[StrictStr] | None = None
    CommunityMatches: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
