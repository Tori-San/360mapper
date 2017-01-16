def lerp(a, b, c):
    return (1-c) * a + c * b


def lerp2d(a00, a10, a01, a11, dx, dy):
    return lerp(
        lerp(a00, a10, dx),
        lerp(a01, a11, dx),
        dy
    )
