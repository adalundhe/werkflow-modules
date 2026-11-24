from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_cluster_peer_authentication_status import FSxClusterPeerAuthenticationStatus
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_tag import FSxTag


class FSxClusterPeer(BaseModel):
    ResourceARN: StrictStr | None = None
    ClusterPeerId: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    Tags: list[FSxTag] | None = None
    PeerAddresses: list[StrictStr] | None = None
    PeerClusterName: StrictStr | None = None
    PassphraseSecretArn: StrictStr | None = None
    AllowedSvmMode: StrictStr | None = None
    AllowedSvmIds: list[StrictStr] | None = None
    Status: StrictStr | None = None
    UUID: StrictStr | None = None
    AuthenticationStatus: FSxClusterPeerAuthenticationStatus | None = None
