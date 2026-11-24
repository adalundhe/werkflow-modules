from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_addon_pod_identity_associations import EKSAddonPodIdentityAssociations
from .eks_resolve_conflicts import EKSResolveConflicts


class EKSUpdateAddonRequest(BaseModel):
    clusterName: StrictStr
    addonName: StrictStr
    addonVersion: StrictStr | None = None
    serviceAccountRoleArn: StrictStr | None = None
    resolveConflicts: EKSResolveConflicts | None = None
    clientRequestToken: StrictStr | None = None
    configurationValues: StrictStr | None = None
    podIdentityAssociations: list[EKSAddonPodIdentityAssociations] | None = None
