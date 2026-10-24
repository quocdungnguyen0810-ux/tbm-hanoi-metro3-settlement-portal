"""Unit tests for analytical settlement engine (Peck & Loganathan-Poulos)."""

import math
import unittest
from scripts.analytical_engine import PeckModel, LoganathanPoulosModel, twin_tunnel_settlement


class TestAnalyticalEngine(unittest.TestCase):

    def setUp(self):
        self.D = 6.30
        self.z0 = 15.0
        self.K = 0.50
        self.VL = 0.01  # 1.0%
        self.nu = 0.35
        self.peck = PeckModel(self.D, self.z0, self.K, self.VL)
        self.lp = LoganathanPoulosModel(self.D, self.z0, self.nu, self.VL)

    def test_peck_symmetry(self):
        for x in [1.0, 5.0, 10.0, 20.0]:
            self.assertAlmostEqual(self.peck.settlement(x), self.peck.settlement(-x), places=7)

    def test_peck_max_settlement_at_center(self):
        self.assertEqual(self.peck.settlement(0.0), self.peck.Smax)
        self.assertTrue(self.peck.settlement(1.0) < self.peck.Smax)

    def test_peck_slope_at_center_is_zero(self):
        self.assertAlmostEqual(self.peck.slope(0.0), 0.0, places=7)

    def test_peck_mass_conservation_trapezoidal(self):
        # Numerical integration of S(x) from -100m to +100m with step dx=0.01m
        dx = 0.01
        num_steps = int(200.0 / dx)
        x_vals = [-100.0 + i * dx for i in range(num_steps + 1)]
        s_vals = self.peck.profile(x_vals)
        
        # Trapezoidal rule
        integral_vs = (s_vals[0] + s_vals[-1]) / 2.0 + sum(s_vals[1:-1])
        integral_vs *= dx
        
        theoretical_vs = self.VL * (math.pi * (self.D ** 2) / 4.0)
        # Relative error should be < 0.01%
        rel_error = abs(integral_vs - theoretical_vs) / theoretical_vs
        self.assertLess(rel_error, 1e-4, f"Mass conservation violated: rel_error={rel_error}")

    def test_peck_curvature_inflection_point(self):
        # At inflection point x = i, curvature should be 0
        i = self.peck.i
        self.assertAlmostEqual(self.peck.curvature(i), 0.0, places=6)
        self.assertAlmostEqual(self.peck.curvature(-i), 0.0, places=6)

    def test_lp_symmetry(self):
        for x in [2.0, 8.0, 15.0]:
            self.assertAlmostEqual(self.lp.settlement(x), self.lp.settlement(-x), places=7)

    def test_twin_tunnel_superposition(self):
        d = 13.0
        # Peak at midpoint or twin peaks
        s_mid = twin_tunnel_settlement(self.peck, self.peck, d, 0.0)
        s_single = self.peck.settlement(0.0)
        self.assertGreater(s_mid, s_single)


if __name__ == "__main__":
    unittest.main()
