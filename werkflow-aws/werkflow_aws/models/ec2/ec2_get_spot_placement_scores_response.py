from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_spot_placement_score import EC2SpotPlacementScore


class EC2GetSpotPlacementScoresResponse(BaseModel):
    SpotPlacementScores: list[EC2SpotPlacementScore] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
