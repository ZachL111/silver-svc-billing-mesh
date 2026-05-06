"""Executable checks for the silver-svc-billing-mesh casebook."""

from __future__ import annotations

from collections import Counter

from . import silver_svc_billing_mesh_segment_00
from . import silver_svc_billing_mesh_segment_01
from . import silver_svc_billing_mesh_segment_02
from . import silver_svc_billing_mesh_segment_03
from . import silver_svc_billing_mesh_segment_04
from . import silver_svc_billing_mesh_segment_05
from . import silver_svc_billing_mesh_segment_06
from . import silver_svc_billing_mesh_segment_07
from . import silver_svc_billing_mesh_segment_08
from . import silver_svc_billing_mesh_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from silver_svc_billing_mesh_segment_00.iter_silver_svc_billing_mesh_00()
    yield from silver_svc_billing_mesh_segment_01.iter_silver_svc_billing_mesh_01()
    yield from silver_svc_billing_mesh_segment_02.iter_silver_svc_billing_mesh_02()
    yield from silver_svc_billing_mesh_segment_03.iter_silver_svc_billing_mesh_03()
    yield from silver_svc_billing_mesh_segment_04.iter_silver_svc_billing_mesh_04()
    yield from silver_svc_billing_mesh_segment_05.iter_silver_svc_billing_mesh_05()
    yield from silver_svc_billing_mesh_segment_06.iter_silver_svc_billing_mesh_06()
    yield from silver_svc_billing_mesh_segment_07.iter_silver_svc_billing_mesh_07()
    yield from silver_svc_billing_mesh_segment_08.iter_silver_svc_billing_mesh_08()
    yield from silver_svc_billing_mesh_segment_09.iter_silver_svc_billing_mesh_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def silver_svc_billing_mesh_summary() -> dict:
    return assert_expected()
