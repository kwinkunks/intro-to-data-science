def gardner(vp: float,
            alpha: float = 0.310,
            beta: float = 0.25
            ) -> float:
    """
    Implements the Gardner equation for estimating
    bulk density, rho, from P-wave velocity Vp.

    Args:
        vp (float): P-wave velocity in m/s.
        alpha (float): First parameter, default 0.31.
        beta (float): Second parameter, default 0.25.

    Returns:
        float: Bulk density in g/cm³.

    Example:
        >>> x = gardner(2000)
        >>> abs(x - 2.0730949) < 1e-6
        True
    """
    return alpha * vp**beta
