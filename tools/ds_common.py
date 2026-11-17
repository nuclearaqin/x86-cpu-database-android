# -*- coding: utf-8 -*-
"""Shared helpers for the incremental CPU dataset (2018-11 -> 2026-11)."""


def C(model, ym, cores, threads, base, boost, tdp, l3, **ov):
    """One CPU row.

    model   : model name without the vendor prefix
    ym      : (year, month) launch date, used for both `launch` formats
    base    : base clock in MHz
    boost   : boost clock in MHz (== base when the part has no turbo)
    l3      : L3 cache in KB
    """
    return dict(model=model, ym=ym, cores=cores, threads=threads,
                base=base, boost=boost, tdp=tdp, l3=l3, **ov)


def S(vendor, product, name, order, defaults, cpus):
    """One series plus the CPUs that belong to it."""
    return dict(vendor=vendor, product=product, name=name, order=order,
                defaults=defaults, cpus=cpus)


# ---------------------------------------------------------------- ISA / feature strings
ISA_INTEL_9 = ("MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AES, AVX, AVX2, BMI1, BMI2, "
               "F16C, FMA3, TXT, EM64T")
ISA_INTEL_512 = ("MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AES, AVX, AVX2, AVX-512, "
                 "BMI1, BMI2, F16C, FMA3, TXT, EM64T")
ISA_INTEL_ADL = ("MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AES, AVX, AVX2, AVX-VNNI, "
                 "BMI1, BMI2, F16C, FMA3, SHA, EM64T")
ISA_INTEL_ARL = ("MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AES, AVX, AVX2, AVX-VNNI, "
                 "AVX-VNNI-INT8, BMI1, BMI2, F16C, FMA3, SHA, EM64T")
ISA_AMD_ZEN = ("MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, SSE4a, AES, AVX, AVX2, "
               "BMI1, BMI2, F16C, FMA3, SHA, ABM, AMD64")
ISA_AMD_ZEN4 = ("MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, SSE4a, AES, AVX, AVX2, "
                "AVX-512, BMI1, BMI2, F16C, FMA3, SHA, ABM, AMD64")
ISA_AMD_OLD = ("MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, SSE4a, AES, AVX, AVX2, "
               "BMI1, F16C, FMA3, SHA, ABM, AMD64")

FEAT_HT = "HyperThreading, NX bit, VT-x, VT-d"
FEAT_HT_NOVT = "HyperThreading, NX bit, VT-x"
FEAT_PLAIN = "NX bit, VT-x, VT-d"
FEAT_PLAIN2 = "NX bit, VT-x"
FEAT_AMD_SMT = "NX bit, AMD-V, SMT"
FEAT_AMD = "NX bit, AMD-V"

PCIE_CFG16 = "x16, x8, x4, x2, x1"
PCIE_CFG20 = "1x16+1x4, 2x8+1x4, 1x8+3x4"
PCIE_CFG24 = "1x16+1x4+1x4, 2x8+1x4+1x4, 1x8+3x4+1x4"
PCIE_CFG_TR = "x16, x8, x4, x2, x1"
