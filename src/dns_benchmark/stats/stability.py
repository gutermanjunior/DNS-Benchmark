def compute_stability(samples):
    grouped = {}

    for s in samples:
        key = (s.resolver, s.test_type)
        grouped.setdefault(key, []).append(s)

    results = {}

    for (resolver, test_type), entries in grouped.items():
        latencies = [s.latency for s in entries if s.success]
        failures = len([s for s in entries if not s.success])

        total = len(entries)
        failure_rate = failures / total if total else 0

        if latencies:
            mean = sum(latencies) / len(latencies)
            std = (sum((x - mean) ** 2 for x in latencies) / len(latencies)) ** 0.5
            cv = std / mean if mean > 0 else 0
        else:
            cv = None

        results[(resolver, test_type)] = {
            "failure_rate": failure_rate,
            "cv": cv
        }

    return results