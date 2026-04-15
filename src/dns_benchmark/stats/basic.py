import statistics
from typing import List, Dict
from dns_benchmark.models.sample import Sample
from dns_benchmark.stats.percentiles import percentile


def compute_basic_stats(samples: List[Sample]) -> Dict:
    grouped = {}

    for s in samples:
        if s.success:
            key = (s.resolver, s.test_type)
            grouped.setdefault(key, []).append(s.latency)

    results = {}

    for (resolver, test_type), values in grouped.items():
        results[(resolver, test_type)] = {
            "mean": statistics.mean(values),
            "min": min(values),
            "max": max(values),
            "std": statistics.pstdev(values) if len(values) > 1 else 0,
            "p95": percentile(values, 95),
            "count": len(values)
        }

    return results