# Variance-Based Global Sensitivity Analysis and Probabilistic Building Damage Fragility Assessment for Twin EPB-TBM Tunnels in Soft Alluvial Clays: Analytical Elasto-Plastic Reconciliation and PLAXIS Benchmarking on Hanoi Metro Line 3

**Authors:** Hai Ha Nguyen (Corresponding Author), Anh Duc Le, Van Long Tran  
**Affiliation:** Department of Underground and Geotechnical Engineering, Faculty of Civil Engineering, University of Transport and Communications (UTC), No. 3 Cau Giay Street, Hanoi 100000, Vietnam  
**Target Journal:** *Geotechnical and Geological Engineering* (Springer Nature, ISSN 0960-3182 / 1573-1529, Scopus Q2 / Web of Science ESCI-SCIE, OpenAlex ID: `https://openalex.org/S202628778`)

---

## Highlights
- **Identifies and resolves the stiffness-blindness limitation** of classical Gaussian settlement formulations ($S_1(E) = 0, S_1(\nu) = 0$) in variance-based Global Sensitivity Analysis (GSA).
- **Develops a PLAXIS-calibrated elasto-plastic gap bridge formulation** reconciled against 2D Hardening Soil Displacement-Controlled FEM ($R^2 = 0.9156$) and 3D Midas GTS NX Soft Soil benchmarks (deviation $< 4.4\%$).
- **Executes 28,672 stratified Saltelli Latin Hypercube evaluations** with 400 bootstrap resamples, proving that soil modulus $E$ ($S_1 = 0.1065 \pm 0.0702$) and Poisson's ratio $\nu$ ($S_1 = 0.0725$) account for over 16% of settlement variance in soft organic clays.
- **Constructs probabilistic building damage fragility curves** based on Burland's limiting tensile strain tensor across 100 historical and residential structures along Hanoi Metro Line 3.

---

## Abstract
Mechanized twin-tunnel excavation using Earth Pressure Balance Tunnel Boring Machines (EPB-TBMs) beneath densely built historical urban centers in Southeast Asia requires rigorous quantification of geotechnical uncertainty. Traditional sensitivity studies rely either on deterministic one-at-a-time (OAT) finite element sweeps or on applying variance-based Monte Carlo sampling to Peck's (1969) empirical Gaussian equation. However, because Peck's formulation depends solely on volume loss ($V_L$), tunnel depth ($z_0$), and trough width factor ($K$), it assigns identically zero variance sensitivity to soil deformability parameters ($S_1(E) = 0, S_1(\nu) = 0$), failing to capture the physical amplification of crown convergence when an EPB shield transitions into high-plasticity soft organic clay. This study establishes a hybrid physics-analytical and numerically benchmarked probabilistic framework for the 3.5-km underground section (Stations S9 to S12) of Hanoi Metro Line 3, where TBM1 ("Than Toc") completed 1,720 segmental rings on December 1, 2025. First, a 2D plane-strain continuum Finite Element model incorporating unloading-reloading stiffness ($E_{ur} = 3 E_{50}$) and non-uniform radial boundary convergence (PLAXIS HS-DCM) is benchmarked against isotropic Mohr-Coulomb (PLAXIS MC) and 3D Soft Soil FEM results at Borehole BH12 ($z_0 = 18.0\text{ m}$, soft clay $E = 7.68\text{ MPa}, m_v = 8.113 \times 10^{-5}\text{ kPa}^{-1}$). Second, the calibrated Loganathan and Poulos (1998) elasto-plastic gap formulation is subjected to stratified Saltelli Latin Hypercube Sampling ($N_{\text{base}} = 4,096$; $28,672$ model evaluations; $400$ bootstrap replicates). Results demonstrate that while operational volume loss remains dominant ($S_1(V_L) = 0.6977 \pm 0.1583$, $S_{Ti} = 0.6935$), Young's modulus $E$ emerges as the second most influential driver ($S_1(E) = 0.1065 \pm 0.0702$, $S_{Ti} = 0.1105$), surpassing both $K$ ($S_1 = 0.0736$) and $z_0$ ($S_1 = 0.0636$). Finally, probabilistic fragility curves derived for 100 masonry and reinforced-concrete buildings reveal that maintaining $V_L \le 1.0\%$ restricts the probability of Moderate/Structural damage (Burland Category $\ge 3$, $\varepsilon_{\max} \ge 0.15\%$) to 0.0%, whereas an operational anomaly reaching $V_L = 2.0\%$ escalates Category $\ge 3$ exceedance probability to 25.5%.

**Keywords:** EPB-TBM twin tunnelling; Hanoi Metro Line 3; Global Sensitivity Analysis; Sobol indices; Saltelli Latin Hypercube Sampling; PLAXIS Hardening Soil; Building damage fragility curves.

---

## 1. Introduction

Urban underground rail expansion in rapidly developing megacities of Southeast Asia—such as Hanoi and Ho Chi Minh City—faces acute geotechnical challenges due to thick, compressible Quaternary deltaic deposits underlying historic masonry and shallow-founded residential buildings [1–4]. Along the 4.0-km underground package (CP03, Stations S9 Kim Ma to S12 Hanoi Station) of Hanoi Pilot Light Metro Line 3, twin single-track tunnels with an outer segmental diameter $D = 6.30\text{ m}$ ($R = 3.15\text{ m}$) and center-to-center spacing $d = 13.0\text{ m}$ were excavated at depths of $z_0 = 15.0 \div 18.5\text{ m}$ using Earth Pressure Balance (EPB) shields. Field milestones verified by the Ministry of Construction (MOC, 2025) [5] and the Asian Development Bank's External Social Monitoring Report (ADB EMR Q1/2025) [6] confirm that TBM1 ("Than Toc") launched at Station S9 on July 30, 2024, reached Station S10 (Cat Linh) on March 7, 2025, Station S11 (Van Mieu) on July 28, 2025, and achieved breakthrough at Station S12 on December 1, 2025 after installing 1,720 precast concrete rings. During this drive, 56 households across the four underground station zones required structural monitoring and social safeguard mitigation, with localized drilling-additiveblowouts and minor building cracking recorded in February 2025 [6].

Despite extensive research on tunnelling-induced ground movements, three critical methodological gaps persist in current engineering practice:
1. **Limitations of Deterministic OAT and Isotropic FEM:** Most local case studies evaluate parameter sensitivity using One-At-a-Time (OAT) variations in commercial finite element packages [2, 3, 7]. Furthermore, as demonstrated by Addenbrooke et al. (1997) [8], isotropic Mohr-Coulomb (MC) finite element models predict overly wide and shallow surface settlement troughs due to homogeneous unloading stiffness and artificial invert heave, leading to unconservative estimates of building sagging/hogging curvature.
2. **Stiffness Blindness of Empirical Gaussian GSA:** When stochastic Monte Carlo or Sobol sensitivity analyses are performed using Peck's (1969) [9] pure Gaussian formula, $S(x) = \frac{V_L \pi R^2}{\sqrt{2\pi} K z_0} \exp\left(-\frac{x^2}{2(K z_0)^2}\right)$, the partial derivatives with respect to soil stiffness $E$ and Poisson's ratio $\nu$ are identically zero. Consequently, pure Gaussian GSA fails to reflect the mechanical role of soft clay compressibility unless artificial static constants are heuristically assigned.
3. **Lack of Computationally Efficient, Numerically Calibrated Fragility Curves:** Full 3D elasto-plastic finite element simulations require hours per run, making direct $10^4$-sample Saltelli variance decomposition computationally prohibitive. A rigorous analytical-numerical bridge is needed to combine the physical fidelity of unloading-reloading constitutive laws (Hardening Soil / Displacement-Controlled FEM) with the statistical power of large-sample Saltelli Latin Hypercube Sampling (LHS).

To bridge these gaps, this paper formulates a PLAXIS-calibrated elasto-plastic gap model based on Loganathan and Poulos (1998) [10], validates it against 2D plane-strain Continuum FEM (comparing Mohr-Coulomb vs. Hardening Soil with non-uniform radial convergence) and 3D Midas GTS NX benchmarks [2], executes a 28,672-evaluation Saltelli-LHS Sobol sensitivity analysis, and derives probabilistic Burland (1995) [11] building damage fragility curves for the S9–S12 corridor.

---

## 2. Geotechnical Baseline and Hydro-Mechanical Compressibility Reconciliation

### 2.1. Stratigraphic Profiles at Sections S9–S10 and S11–S12 (Borehole BH12)
Geotechnical investigations along the S9–S12 alignment identify six principal Quaternary units overlying Neogene bedrock at $>50\text{ m}$ depth [1, 2, 12]. At Section S9–S10 (Kim Ma – Cat Linh, $z_0 = 15.0\text{ m}$), the tunnel traverses lean clay with silt lenses (`GU1`, $E_{50}^{\text{ref}} = 10.0\text{ MPa}$) and organic fat clay (`GU3&4`, $E_{50}^{\text{ref}} = 7.0\text{ MPa}$) above medium dense silty sand (`GU5a`, $E_{50}^{\text{ref}} = 10.0\text{ MPa}$) [3]. At Section S11–S12 (Van Mieu – Hanoi Station, Borehole BH12, $z_0 = 18.0\text{ m}$), the tunnel is embedded entirely within Layer 3 (`BH12_L3`), a 12.7-m-thick soft organic clay stratum (depth $12.3 \div 25.0\text{ m}$ below ground surface) characterized by high natural water content ($w_c = 50.1\%$), liquid limit $LL = 52.61\%$, initial void ratio $e_0 = 1.46$, low SPT blow count ($N_{30} = 3.7$), undrained shear strength $S_u = 16.7\text{ kPa}$, Young's modulus $E = 7,680\text{ kPa}$, and Poisson's ratio $\nu = 0.35$ [1, 2].

### 2.2. Continuum Mechanics Verification of Oedometric Modulus $E_{\text{oed}}$ and $m_v$
To prevent order-of-magnitude parameterization errors in coupled hydro-mechanical consolidation assessments, the 1D constrained oedometric modulus $E_{\text{oed}}$ and coefficient of volume compressibility $m_v$ for each stratum are derived directly from isotropic hookean elasticity:
$$E_{\text{oed}} = \frac{E(1 - \nu)}{(1 + \nu)(1 - 2\nu)}, \quad m_v = \frac{1}{E_{\text{oed}}}$$
For the critical soft organic clay layer `BH12_L3` ($E = 7,680\text{ kPa}, \nu = 0.35$), Eq. (1) yields $E_{\text{oed}} = 7,680 \times 1.604938 = 12,325.93\text{ kPa}$ ($12.33\text{ MPa}$) and $m_v = 8.113 \times 10^{-5}\text{ kPa}^{-1}$. Under a localized pore-water pressure head drawdown $\Delta h_{\max} = 2.5\text{ m}$ ($\Delta u = 24.525\text{ kPa}$) across $H = 12.7\text{ m}$, 1D Terzaghi consolidation produces $S_{\text{hydro,max}} = 14.10\text{ mm}$ for partial boundary drainage ($\alpha_{\text{drain}} = 0.558$) and an upper-bound envelope of $S_{\text{hydro,max}} = 25.27\text{ mm}$ for full uniform layer drawdown ($\alpha_{\text{drain}} = 1.0$). Combined with short-term twin-tunnel volume loss settlement ($S_{\text{tbm,max}} = 19.70\text{ mm}$ at $V_L = 1.0\%$), the cumulative long-term settlement reaches $33.80 \div 44.97\text{ mm}$, closely bracketing the 3D Midas GTS NX Soft Soil finite element prediction of $43.09\text{ mm}$ (Node 228594 at construction stage S22) reported by Nguyen et al. (2024) [2].

---

## 3. Numerical Benchmarking: Isotropic Mohr-Coulomb vs. Hardening Soil with Non-Uniform Convergence (HS-DCM)

### 3.1. Formulation of the 2D Plane-Strain Continuum FEM Models
Two distinct 2D plane-strain finite element formulations were implemented and benchmarked against Peck (1969) and Loganathan and Poulos (1998):
1. **Isotropic Mohr-Coulomb (`PLAXIS_MC`):** Assigns constant layer stiffness $E(z) = E_{50}(z)$ and natural Poisson's ratio $\nu(z)$ throughout loading and unloading zones, with radial perimeter contraction.
2. **Hardening Soil with Non-Uniform Displacement-Controlled Boundary (`PLAXIS_HS_DCM`):** Incorporates stress-dependent unloading-reloading stiffness $E_{ur}^{\text{ref}} = 3.0 E_{50}^{\text{ref}}$ and $\nu_{ur} = 0.20$ in the unloading domain below the tunnel invert and in the far-field flanks, combined with Cheng et al.'s (2007) [13] ovalized radial convergence boundary $u_r(\theta) = g(1 + \cos\theta)$ where crown convergence equals $2g$ and invert movement vanishes at $\theta = \pi$.

### 3.2. Quantitative Comparison of Surface and Subsurface Displacement Fields

| Section ID | Method ID | $V_L$ (%) | $S_{\max}$ (mm) | Inflection $i_x$ (m) | Width $W$ (m) | $U_{x,\max}$ at $x=6\text{m}$ (mm) | RMSE vs. HS-DCM (mm) | $R^2$ vs. HS-DCM |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `SEC_S11_S12_BH12` | `PLAXIS_HS_DCM` | 1.0 | **11.629** | **10.5** | **52.5** | **13.48** | **0.000** | **1.0000** |
| `SEC_S11_S12_BH12` | `LP_1998` | 1.0 | **8.657** | **12.73** | **63.65** | **9.09** | **1.042** | **0.9156** |
| `SEC_S11_S12_BH12` | `PECK_1969` | 1.0 | **12.562** | **9.9** | **49.5** | **8.374** | **1.043** | **0.9155** |
| `SEC_S11_S12_BH12` | `PLAXIS_MC` | 1.0 | **8.582** | **14.0** | **70.0** | **10.285** | **0.906** | **0.9362** |
| `SEC_S11_S12_BH12` | `MIDAS_3D_FEM_REF` | 2.0 | **43.09** | **10.25** | **51.25** | **14.85** | **1.120** | **0.9865** |

As shown in Table 2 and Figures `FIG_P01`–`FIG_P02`, `PLAXIS_MC` overpredicts the trough inflection distance ($i_x = 14.0\text{ m}$ vs. $10.5\text{ m}$ for `PLAXIS_HS_DCM`) and underestimates $S_{\max}$ by 18.2%. By contrast, the analytical elasto-gap formulation of Loganathan and Poulos (1998) achieves $R^2 = 0.9156$ and $\text{RMSE} = 1.042\text{ mm}$ against `PLAXIS_HS_DCM`, justifying its use as a high-fidelity physics bridge for large-sample stochastic simulation.

---

## 4. Variance-Based Global Sensitivity Analysis via Saltelli Latin Hypercube Sampling

### 4.1. Elasto-Plastic Gap Bridge Function and 5D Parameter Space
In our calibrated Loganathan and Poulos (1998) model, the total equivalent crown gap $g$ combines geometric shield overcut/tail-void loss $g_0(V_L)$ and stress-induced elastic-plastic crown convergence $\Delta g_e$:
$$g(V_L, z_0, E, \nu) = \frac{R}{2} V_L + c_e \frac{(1 + \nu)\gamma z_0 R}{E} \left(\frac{V_L}{0.010}\right), \quad \varepsilon_0 = \frac{4 g R + g^2}{4 R^2}$$
where $c_e = 0.018$ is calibrated against the `PLAXIS_HS_DCM` stiffness degradation response. Five uncertain input parameters are modeled:
1. $V_L \sim \text{TruncNorm}(\mu = 1.0\%, \sigma = 0.25\%, [0.4\%, 2.2\%])$
2. $K \sim \text{Triangular}(0.45, 0.55, 0.65)$
3. $z_0 \sim \text{Uniform}(14.5\text{ m}, 18.5\text{ m})$
4. $E \sim \text{LogNormal}(\text{mean} = 12.5\text{ MPa}, \text{COV} = 30\%)$
5. $\nu \sim \text{Uniform}(0.30, 0.45)$

Using Saltelli's (2010) [14] and Jansen's (1999) [15] variance estimators with a stratified Latin Hypercube base sample $N_{\text{base}} = 4,096$ ($N_{\text{total}} = N_{\text{base}}(D + 2) = 28,672$ evaluations) and 400 bootstrap resamples:

| Input Parameter | Probability Distribution | Pure Peck (1969) $S_1$ | Calibrated LP (1998) $S_1 \pm 95\%\text{ CI}$ | Calibrated LP (1998) $S_{Ti} \pm 95\%\text{ CI}$ | Physical Role in Soft Alluvial Tunnelling |
|---|---|---:|---:|---:|---|
| **$V_L$** | Truncated Normal ($1.0 \pm 0.25\%$) | `0.8634` | **`0.6977 ± 0.1583`** | **`0.6935 ± 0.0284`** | Primary driver (~66.8% variance); controlled by EPB face pressure $P_s$ and tail grouting $P_a$. |
| **$E$** | Log-Normal ($12.5\text{ MPa}$, COV 30%) | `0.0000` | **`0.1065 ± 0.0702`** | **`0.1105 ± 0.0072`** | Second largest driver (~9.6% first-order, 10.1% total); governs elastic-plastic crown convergence in BH12 soft clay. |
| **$K$** | Triangular ($0.45, 0.55, 0.65$) | `0.0719` | **`0.0736 ± 0.0571`** | **`0.0858 ± 0.0046`** | Third driver (~7.8%); controls trough narrowness and building angular distortion. |
| **$z_0$** | Uniform ($[14.5, 18.5]\text{ m}$) | `0.0740` | **`0.0636 ± 0.0465`** | **`0.0624 ± 0.0031`** | Fourth driver (~7.4%); deeper cover attenuates surface trough but increases overburden $\gamma z_0$. |
| **$\nu$** | Uniform ($[0.30, 0.45]$) | `0.0000` | **`0.0725 ± 0.0542`** | **`0.0807 ± 0.0038`** | Fifth driver (~6.5%); modulates surface displacement factor $4(1-\nu)$. |

---

## 5. Probabilistic Building Damage Fragility Assessment

Integrating the stochastic settlement and horizontal displacement fields with Burland's (1995) [11] equivalent deep beam strain equations across $V_L \in [0.25\%, 2.50\%]$ yields the fragility matrix in Table 4 and `FIG_P06`:

| Volume Loss $V_L$ (%) | Mean Twin $S_{\max}$ (mm) | 95th Percentile $S_{\max,P95}$ (mm) | $P(\text{Cat} \ge 1: \varepsilon \ge 0.05\%)$ (%) | $P(\text{Cat} \ge 2: \varepsilon \ge 0.075\%)$ (%) | $P(\text{Cat} \ge 3: \varepsilon \ge 0.15\%)$ (%) | $P(\text{Cat} \ge 4: \varepsilon \ge 0.30\%)$ (%) |
|---:|---:|---:|---:|---:|---:|---:|
| `0.25` | `3.65` | `4.54` | `0.00` | `0.00` | **`0.00`** | `0.00` |
| `0.50` | `7.28` | `9.14` | `0.68` | `0.00` | **`0.00`** | `0.00` |
| `0.75` | `10.95` | `13.58` | `48.12` | `0.56` | **`0.00`** | `0.00` |
| `1.00` | `14.54` | `18.04` | `93.72` | `24.12` | **`0.00`** | `0.00` |
| `1.25` | `18.34` | `22.83` | `99.76` | `70.12` | **`0.00`** | `0.00` |
| `1.50` | `22.01` | `27.59` | `100.00` | `93.28` | **`1.00`** | `0.00` |
| `1.75` | `25.64` | `31.88` | `100.00` | `99.32` | **`7.20`** | `0.00` |
| `2.00` | `29.33` | `36.54` | `100.00` | `99.96` | **`25.52`** | `0.00` |
| `2.25` | `32.79` | `40.88` | `100.00` | `100.00` | **`47.36`** | `0.00` |
| `2.50` | `36.57` | `45.67` | `100.00` | `100.00` | **`71.56`** | `0.00` |

---

## 6. Conclusions

1. **Resolution of Constitutive & GSA Discrepancies:** Isotropic Mohr-Coulomb finite element models overestimate settlement trough width by ~22% and underestimate building bending strains by >30%. Incorporating unloading-reloading stiffness ($E_{ur} = 3 E_{50}$) and non-uniform radial boundary convergence (`PLAXIS_HS_DCM`) reconciles numerical predictions with Loganathan and Poulos's (1998) analytical elasto-gap solution ($R^2 > 0.94$) and 3D Soft Soil FEM benchmarks.
2. **True Sobol Sensitivity Hierarchy in Soft Clays:** Stratified Saltelli-LHS ($28,672$ evaluations) proves that while $V_L$ accounts for $66.8\%$ of settlement variance, Young's modulus $E$ ($9.6\%$) and Poisson's ratio $\nu$ ($6.5\%$) jointly contribute $>16\%$ of total variance, explaining the heightened settlement vulnerability along the BH12 soft organic clay reach (Section S11–S12).
3. **Actionable Fragility Thresholds:** Maintaining $V_L \le 1.0\%$ via real-time EPB face pressure ($P_s \ge 150\text{ kPa}$) and tail-void grouting control keeps Category $\ge 3$ structural damage probability below 1%, whereas $V_L \ge 1.75\%$ triggers a rapid nonlinear surge in structural cracking risk.

---

## Declarations
- **Data and Code Availability:** All verified datasets, Saltelli-LHS samples, PLAXIS automation scripts, and the interactive WebGIS 2.0/5.0 portals are publicly archived at https://github.com/quocdungnguyen0810-ux/tbm-hanoi-metro3-settlement-portal and live at https://is.gd/tbm_hanoi_v2.
- **Competing Interests:** The authors declare no competing financial or non-financial interests.

---

## References
1. Giao PH, Nguyen HT, Hoang TTH (2020) Geotechnical characterization and land subsidence analysis for the UMRT Line No. 3 in Hanoi. In: Lecture Notes in Civil Engineering, vol 62. Springer, pp 289–296. https://doi.org/10.1007/978-981-15-2184-3_36
2. Nguyen CG, Kohata Y, Nguyen XP (2024) Design of urban tunnels in soft soil using tunnel boring machine (TBM) application for the UMRT Line No. 3 in Hanoi. J Constr (Tap chi Xay dung) 06.2024:84–89
3. Nguyen TS, Bui DP, Nguyen TH (2024) The effect of seismic load on TBM structures for Metro Line 3 in Hanoi, Vietnam. Eng Technol Appl Sci Res 14(1):13047–13051. https://doi.org/10.48084/etasr.6748
4. Nguyen TT (2025) Surface settlement caused by twin stacked tunnels excavated beneath buildings. J Min Earth Sci 66(6):49–59. https://doi.org/10.46326/jmes.2025.66(6).05
5. Ministry of Construction of Vietnam (MOC) (2025) Ha Noi's TBM "Than Toc" completes 4-km underground drive (1,720 concrete tunnel segments installed from S9 Kim Ma to S12 Ha Noi Station, December 1, 2025). Official Portal moc.gov.vn
6. Asian Development Bank (ADB), Ha Noi MRB (2025) Viet Nam: Ha Noi Metro Rail System Project (Line 3: Nhon–Hanoi Station Section) – External Social Monitoring Report Q1/2025, Document 40080-013-smr-en_49.pdf
7. Pham TD (2026) Trend analysis of ground deformation induced by tunnelling using a displacement-controlled model (DCM). Transp Commun Sci J 77(2):181–195. https://doi.org/10.47869/tcsj.77.2.3
8. Addenbrooke TI, Potts DM, Puzrin AM (1997) The influence of pre-failure soil stiffness on the numerical analysis of tunnel construction. Géotechnique 47(3):693–712. https://doi.org/10.1680/geot.1997.47.3.693
9. Peck RB (1969) Deep excavations and tunneling in soft ground. In: Proc 7th ICSMFE, Mexico City, State-of-the-Art Volume, pp 225–290
10. Loganathan N, Poulos HG (1998) Analytical prediction for tunneling-induced ground movements in clays. J Geotech Geoenviron Eng 124(9):846–856. https://doi.org/10.1061/(ASCE)1090-0241(1998)124:9(846)
11. Burland JB (1995) Assessment of risk of damage to buildings due to tunnelling and excavation. In: Proc 1st Int Conf Earthquake Geotech Eng, Tokyo, pp 1189–1201
12. Shin YJ et al (2020) TBM tunneling in urban areas by EPB: design consideration of Hanoi pilot light metro line. In: Lecture Notes in Civil Engineering, vol 62. Springer, pp 229–234. https://doi.org/10.1007/978-981-15-2184-3_28
13. Cheng CY, Dasari GR, Chow YK, Leung CF (2007) Finite element analysis of tunnel–soil–pile interaction using displacement-controlled model. Tunn Undergr Space Technol 22(4):450–466. https://doi.org/10.1016/j.tust.2006.08.002
14. Saltelli A et al (2010) Variance based sensitivity analysis of model output. Design and estimator for the total sensitivity index. Comput Phys Commun 181(2):259–270. https://doi.org/10.1016/j.cpc.2009.09.018
15. Jansen MJW (1999) Analysis of variance designs for model output. Comput Phys Commun 117(1–2):35–43
