"""Analytical settlement calculation engine for Peck (1969) and Loganathan & Poulos (1998).

Implements single tunnel and twin tunnel superposition, slope/tilt, and curvature.
Convention: settlement S is positive downwards (m).
Volume loss VL is input as decimal ratio (e.g. 0.01 for 1.0%).
"""

import math
from typing import Dict, List, Tuple


class PeckModel:
    """Peck (1969) Gaussian settlement trough model."""

    def __init__(self, D: float, z0: float, K: float, VL: float):
        """
        D: Tunnel outer diameter (m)
        z0: Tunnel axis depth (m)
        K: Trough width parameter (dimensionless)
        VL: Volume loss ratio (e.g. 0.01 for 1.0%)
        """
        assert D > 0, "Diameter must be positive"
        assert z0 > D / 2.0, "Depth must be greater than tunnel radius"
        assert K > 0, "Trough parameter K must be positive"
        assert 0.0 < VL <= 0.10, "Volume loss VL must be a decimal fraction <= 0.10"
        
        self.D = D
        self.z0 = z0
        self.K = K
        self.VL = VL
        
        # Trough width i (m)
        self.i = self.K * self.z0
        # Tunnel cross-sectional area At (m^2)
        self.At = math.pi * (self.D ** 2) / 4.0
        # Maximum surface settlement Smax (m)
        # Vs = sqrt(2*pi)*i*Smax = VL * At ==> Smax = (VL * At) / (sqrt(2*pi) * i)
        self.Smax = (self.VL * self.At) / (math.sqrt(2.0 * math.pi) * self.i)

    def settlement(self, x: float) -> float:
        """Surface settlement at offset x from tunnel centerline (m)."""
        return self.Smax * math.exp(-(x ** 2) / (2.0 * (self.i ** 2)))

    def slope(self, x: float) -> float:
        """First derivative dS/dx (tilt). Sign indicates direction of slope."""
        return - (x / (self.i ** 2)) * self.settlement(x)

    def curvature(self, x: float) -> float:
        """Second derivative d^2S/dx^2 (curvature)."""
        return ((x ** 2 - self.i ** 2) / (self.i ** 4)) * self.settlement(x)

    def profile(self, x_coords: List[float]) -> List[float]:
        return [self.settlement(x) for x in x_coords]


class LoganathanPoulosModel:
    """Loganathan & Poulos (1998) analytical solution for surface settlement.
    
    Marked with qa_flag: secondary_source_unverified_original.
    """

    def __init__(self, D: float, z0: float, nu: float, VL: float):
        """
        D: Tunnel outer diameter (m)
        z0: Tunnel axis depth (m)
        nu: Poisson's ratio
        VL: Equivalent ground loss ratio epsilon0
        """
        assert D > 0, "Diameter must be positive"
        assert z0 > D / 2.0, "Depth must be greater than tunnel radius"
        assert 0.0 <= nu < 0.5, "Poisson ratio must be < 0.5"
        assert 0.0 < VL <= 0.10, "VL must be decimal ratio"
        
        self.D = D
        self.R = D / 2.0
        self.z0 = z0
        self.nu = nu
        self.VL = VL

    def settlement(self, x: float) -> float:
        """Surface settlement at x (m)."""
        # S(x) = epsilon0 * R^2 * [4*(1-nu)*z0 / (x^2 + z0^2)] * exp(-1.38*x^2 / (z0 + R)^2)
        term1 = self.VL * (self.R ** 2)
        term2 = (4.0 * (1.0 - self.nu) * self.z0) / (x ** 2 + self.z0 ** 2)
        term3 = math.exp(-1.38 * (x ** 2) / ((self.z0 + self.R) ** 2))
        return term1 * term2 * term3

    def profile(self, x_coords: List[float]) -> List[float]:
        return [self.settlement(x) for x in x_coords]


def twin_tunnel_settlement(model_left, model_right, d: float, x: float) -> float:
    """Linear superposition of twin tunnels separated by center-to-center distance d (m).
    
    Left tunnel at x = -d/2, Right tunnel at x = +d/2.
    """
    s_left = model_left.settlement(x + d / 2.0)
    s_right = model_right.settlement(x - d / 2.0)
    return s_left + s_right
