from enum import Enum


class ArchitectureType(Enum):
    ARM_64 = 'arm64'
    x86_64 = 'x86_64'
    AMD_64 = 'AMD64'
    AARCH64 = 'aarch64'
    I386 = 'i386'
    I686 = 'i686'
    X86 = 'x86'
    ARMV7L = 'armv7l'
    ARMV6L = 'armv6l'
    PPC64LE = 'ppc64le'
    S390X = 's390x'
    RISCV64 = 'riscv64'
