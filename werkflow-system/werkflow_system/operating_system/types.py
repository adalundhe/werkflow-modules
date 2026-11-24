from enum import Enum


class OperatingSystemType(Enum):
    MAC_OS = 'Darwin'
    WINDOWS = 'Windows'
    LINUX = 'Linux'


class LinuxDistroFamily(Enum):
    DEBIAN = 'debian'
    REDHAT = 'rhel'
    AMAZON = 'amzn'
    ARCH = 'arch'
    ALPINE = 'alpine'
    SUSE = 'suse'
    GENTOO = 'gentoo'
    VOID = 'void'
    NIXOS = 'nixos'
    SLACKWARE = 'slackware'
    GENERIC = 'linux'
