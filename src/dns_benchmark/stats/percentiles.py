def percentile(data, p):
    if not data:
        return None

    data = sorted(data)
    k = (len(data) - 1) * (p / 100)
    f = int(k)
    c = min(f + 1, len(data) - 1)

    if f == c:
        return data[int(k)]

    d0 = data[f] * (c - k)
    d1 = data[c] * (k - f)
    return d0 + d1