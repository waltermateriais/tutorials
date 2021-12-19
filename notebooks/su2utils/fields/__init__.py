# -*- coding: utf-8 -*-

# TODO: make wrapper for automatic edition of FILE_HEADER
# https://raw.githubusercontent.com/su2code/SU2/master/config_template.cfg

from textwrap import dedent
from ..su2configfield import SU2ConfigField

__all__ = [
    "problem",
    "solver_control",
    "time_dependent",
    "compressible",
    "incompressible",
    "reference_value",
    "boundary_condition",
    "surfaces",
    "common",
    "limiter",
    "linear_solver",
    "multigrid",
    "flow_numerical",
    "file_io"
]


def get_module_docs(module):
    """ Print documentation for a sub-module. """
    for name in dir(module):
        the_attr = getattr(module, name)
        if isinstance(the_attr, SU2ConfigField):
            print(repr(the_attr))


# ------------- DIRECT, ADJOINT, AND LINEARIZED PROBLEM DEFINITION ------------

from . import problem

# ------------------------------- SOLVER CONTROL ------------------------------

from . import solver_control

# ------------------------- TIME-DEPENDENT SIMULATION -------------------------

from . import time_dependent

# ------------------------------- DES Parameters ------------------------------

# % Specify Hybrid RANS/LES model (SA_DES, SA_DDES, SA_ZDES, SA_EDDES)
# HYBRID_RANSLES= SA_DDES

# % DES Constant (0.65)
# DES_CONST= 0.65

# -------------------- COMPRESSIBLE FREE-STREAM DEFINITION --------------------

from . import compressible

# ---------------- INCOMPRESSIBLE FLOW CONDITION DEFINITION -------------------

from . import incompressible

# ----------------------------- SOLID ZONE HEAT VARIABLES-----------------------

# % Thermal conductivity used for heat equation
# THERMAL_CONDUCTIVITY_CONSTANT= 0.0

# % Solids temperature at freestream conditions
# FREESTREAM_TEMPERATURE= 288.15

# % Density used in solids
# MATERIAL_DENSITY= 2710.0

# ----------------------------- CL DRIVER DEFINITION ---------------------------

# % Activate fixed lift mode (specify a CL instead of AoA, NO/YES)
# FIXED_CL_MODE= NO

# % Target coefficient of lift for fixed lift mode (0.80 by default)
# TARGET_CL= 0.80

# % Estimation of dCL/dAlpha (0.2 per degree by default)
# DCL_DALPHA= 0.2

# % Maximum number of iterations between AoA updates
# UPDATE_AOA_ITER_LIMIT= 100

# % Number of iterations to evaluate dCL_dAlpha by using finite differences (500 by default)
# ITER_DCL_DALPHA= 500

# ---------------------- REFERENCE VALUE DEFINITION ---------------------------

from . import reference_value

# ---- NONEQUILIBRIUM GAS, IDEAL GAS, POLYTROPIC, VAN DER WAALS AND PENG ROBINSON CONSTANTS -------

# % Fluid model (STANDARD_AIR, IDEAL_GAS, VW_GAS, PR_GAS,
# %              CONSTANT_DENSITY, INC_IDEAL_GAS, INC_IDEAL_GAS_POLY, MUTATIONPP, SU2_NONEQ)
# FLUID_MODEL= STANDARD_AIR

# % Ratio of specific heats (1.4 default and the value is hardcoded
# %                          for the model STANDARD_AIR, compressible only)
# GAMMA_VALUE= 1.4

# % Specific gas constant (287.058 J/kg*K default and this value is hardcoded
# %                        for the model STANDARD_AIR, compressible only)
# GAS_CONSTANT= 287.058

# % Critical Temperature (131.00 K by default)
# CRITICAL_TEMPERATURE= 131.00

# % Critical Pressure (3588550.0 N/m^2 by default)
# CRITICAL_PRESSURE= 3588550.0

# % Acentri factor (0.035 (air))
# ACENTRIC_FACTOR= 0.035

# % Specific heat at constant pressure, Cp (1004.703 J/kg*K (air)).
# % Incompressible fluids with energy eqn. (CONSTANT_DENSITY, INC_IDEAL_GAS) and the heat equation.
# SPECIFIC_HEAT_CP= 1004.703

# % Thermal expansion coefficient (0.00347 K^-1 (air))
# % Used with Boussinesq approx. (incompressible, BOUSSINESQ density model only)
# THERMAL_EXPANSION_COEFF= 0.00347

# % Molecular weight for an incompressible ideal gas (28.96 g/mol (air) default)
# MOLECULAR_WEIGHT= 28.96

# % Temperature polynomial coefficients (up to quartic) for specific heat Cp.
# % Format -> Cp(T) : b0 + b1*T + b2*T^2 + b3*T^3 + b4*T^4
# CP_POLYCOEFFS= (0.0, 0.0, 0.0, 0.0, 0.0)

# % Nonequilibrium fluid options
# %
# % Gas model - mixture
# GAS_MODEL= AIR-5

# % Initial gas composition in mass fractions
# GAS_COMPOSITION= (0.77, 0.23, 0.0, 0.0, 0.0)

# % Freeze chemical reactions
# FROZEN_MIXTURE= NO

# --------------------------- VISCOSITY MODEL ---------------------------------

# % Viscosity model (SUTHERLAND, CONSTANT_VISCOSITY, POLYNOMIAL_VISCOSITY).
# VISCOSITY_MODEL= SUTHERLAND

# % Molecular Viscosity that would be constant (1.716E-5 by default)
# MU_CONSTANT= 1.716E-5

# % Sutherland Viscosity Ref (1.716E-5 default value for AIR SI)
# MU_REF= 1.716E-5

# % Sutherland Temperature Ref (273.15 K default value for AIR SI)
# MU_T_REF= 273.15

# % Sutherland constant (110.4 default value for AIR SI)
# SUTHERLAND_CONSTANT= 110.4

# % Temperature polynomial coefficients (up to quartic) for viscosity.
# % Format -> Mu(T) : b0 + b1*T + b2*T^2 + b3*T^3 + b4*T^4
# MU_POLYCOEFFS= (0.0, 0.0, 0.0, 0.0, 0.0)

# --------------------------- THERMAL CONDUCTIVITY MODEL ----------------------

# % Laminar Conductivity model (CONSTANT_CONDUCTIVITY, CONSTANT_PRANDTL,
# % POLYNOMIAL_CONDUCTIVITY).
# CONDUCTIVITY_MODEL= CONSTANT_PRANDTL

# % Molecular Thermal Conductivity that would be constant (0.0257 by default)
# THERMAL_CONDUCTIVITY_CONSTANT= 0.0257

# % Laminar Prandtl number (0.72 (air), only for CONSTANT_PRANDTL)
# PRANDTL_LAM= 0.72

# % Temperature polynomial coefficients (up to quartic) for conductivity.
# % Format -> Kt(T) : b0 + b1*T + b2*T^2 + b3*T^3 + b4*T^4
# KT_POLYCOEFFS= (0.0, 0.0, 0.0, 0.0, 0.0)

# % Definition of the turbulent thermal conductivity model for RANS
# % (CONSTANT_PRANDTL_TURB by default, NONE).
# TURBULENT_CONDUCTIVITY_MODEL= CONSTANT_PRANDTL_TURB

# % Turbulent Prandtl number (0.9 (air) by default)
# PRANDTL_TURB= 0.90

# ----------------------- DYNAMIC MESH DEFINITION -----------------------------

# % Type of dynamic mesh (NONE, RIGID_MOTION, ROTATING_FRAME,
# %                       STEADY_TRANSLATION,
# %                       ELASTICITY, GUST)
# GRID_MOVEMENT= NONE

# % Motion mach number (non-dimensional). Used for initializing a viscous flow
# % with the Reynolds number and for computing force coeffs. with dynamic meshes.
# MACH_MOTION= 0.8

# % Coordinates of the motion origin
# MOTION_ORIGIN= 0.25 0.0 0.0

# % Angular velocity vector (rad/s) about the motion origin
# ROTATION_RATE = 0.0 0.0 0.0

# % Pitching angular freq. (rad/s) about the motion origin
# PITCHING_OMEGA= 0.0 0.0 0.0

# % Pitching amplitude (degrees) about the motion origin
# PITCHING_AMPL= 0.0 0.0 0.0

# % Pitching phase offset (degrees) about the motion origin
# PITCHING_PHASE= 0.0 0.0 0.0

# % Translational velocity (m/s or ft/s) in the x, y, & z directions
# TRANSLATION_RATE = 0.0 0.0 0.0

# % Plunging angular freq. (rad/s) in x, y, & z directions
# PLUNGING_OMEGA= 0.0 0.0 0.0

# % Plunging amplitude (m or ft) in x, y, & z directions
# PLUNGING_AMPL= 0.0 0.0 0.0

# % Type of dynamic surface movement (NONE, DEFORMING,
# %                       MOVING_WALL, FLUID_STRUCTURE, FLUID_STRUCTURE_STATIC,
# %                       AEROELASTIC, EXTERNAL, EXTERNAL_ROTATION,
# %                       AEROELASTIC_RIGID_MOTION)
# SURFACE_MOVEMENT= NONE

# % Moving wall boundary marker(s) (NONE = no marker, ignored for RIGID_MOTION)
# MARKER_MOVING= ( NONE )

# % Coordinates of the motion origin
# SURFACE_MOTION_ORIGIN= 0.25

# % Angular velocity vector (rad/s) about the motion origin
# SURFACE_ROTATION_RATE = 0.0 0.0 0.0

# % Pitching angular freq. (rad/s) about the motion origin
# SURFACE_PITCHING_OMEGA= 0.0 0.0 0.0

# % Pitching amplitude (degrees) about the motion origin
# SURFACE_PITCHING_AMPL= 0.0 0.0 0.0

# % Pitching phase offset (degrees) about the motion origin
# SURFACE_PITCHING_PHASE= 0.0 0.0 0.0

# % Translational velocity (m/s or ft/s) in the x, y, & z directions
# SURFACE_TRANSLATION_RATE = 0.0 0.0 0.0

# % Plunging angular freq. (rad/s) in x, y, & z directions
# SURFACE_PLUNGING_OMEGA= 0.0 0.0 0.0

# % Plunging amplitude (m or ft) in x, y, & z directions
# SURFACE_PLUNGING_AMPL= 0.0 0.0 0.0

# % Move Motion Origin for marker moving (1 or 0)
# MOVE_MOTION_ORIGIN = 0

# ------------------------- BUFFET SENSOR DEFINITION --------------------------

# % Compute the Kenway-Martins separation sensor for buffet-onset detection
# % If BUFFET objective/constraint is specified, the objective is given by
# % the integrated sensor normalized by reference area
# %
# % See doi: 10.2514/1.J055172
# %
# % Evaluate buffet sensor on Navier-Stokes markers  (NO, YES)
# BUFFET_MONITORING= NO

# % Sharpness coefficient for the buffet sensor Heaviside function
# BUFFET_K= 10.0

# % Offset parameter for the buffet sensor Heaviside function
# BUFFET_LAMBDA= 0.0

# -------------- AEROELASTIC SIMULATION (Typical Section Model) ---------------

# % Activated by GRID_MOVEMENT_KIND option
# %
# % The flutter speed index (modifies the freestream condition in the solver)
# FLUTTER_SPEED_INDEX = 0.6

# % Natural frequency of the spring in the plunging direction (rad/s)
# PLUNGE_NATURAL_FREQUENCY = 100

# % Natural frequency of the spring in the pitching direction (rad/s)
# PITCH_NATURAL_FREQUENCY = 100

# % The airfoil mass ratio
# AIRFOIL_MASS_RATIO = 60

# % Distance in semichords by which the center of gravity lies behind
# % the elastic axis
# CG_LOCATION = 1.8

# % The radius of gyration squared (expressed in semichords)
# % of the typical section about the elastic axis
# RADIUS_GYRATION_SQUARED = 3.48

# % Solve the aeroelastic equations every given number of internal iterations
# AEROELASTIC_ITER = 3

# --------------------------- GUST SIMULATION ---------------------------------

# % Apply a wind gust (NO, YES)
# WIND_GUST = NO

# % Type of gust (NONE, TOP_HAT, SINE, ONE_M_COSINE, VORTEX, EOG)
# GUST_TYPE = NONE

# % Direction of the gust (X_DIR or Y_DIR)
# GUST_DIR = Y_DIR

# % Gust wavelenght (meters)
# GUST_WAVELENGTH= 10.0

# % Number of gust periods
# GUST_PERIODS= 1.0

# % Gust amplitude (m/s)
# GUST_AMPL= 10.0

# % Time at which to begin the gust (sec)
# GUST_BEGIN_TIME= 0.0

# % Location at which the gust begins (meters) */
# GUST_BEGIN_LOC= 0.0

# ------------------------ SUPERSONIC SIMULATION ------------------------------
# % MARKER_NEARFIELD needs to be defined on a circumferential boundary within
# % calculation domain so that it captures pressure disturbance from the model.
# % The boundary should have a structured grid with the same number of nodes
# % along each azimuthal angle.
# % To run inverse design using target equivalent area, TargetEA.dat is required.
# %
# % Evaluate equivalent area on the Near-Field (NO, YES)
# EQUIV_AREA= NO

# % Integration limits of the equivalent area ( xmin, xmax, Dist_NearField )
# EA_INT_LIMIT= ( 1.6, 2.9, 1.0 )

# % Equivalent area scale factor ( EA should be ~ force based objective functions )
# EA_SCALE_FACTOR= 1.0

# % Fix an azimuthal line due to misalignments of the near-field
# FIX_AZIMUTHAL_LINE= 90.0

# % Drag weight in sonic boom Objective Function (from 0.0 to 1.0)
# DRAG_IN_SONICBOOM= 0.0

# -------------------------- ENGINE SIMULATION --------------------------------

# % Highlite area to compute MFR (1 in2 by default)
# HIGHLITE_AREA= 1.0

# % Fan polytropic efficiency (1.0 by default)
# FAN_POLY_EFF= 1.0

# % Only half engine is in the computational grid (NO, YES)
# ENGINE_HALF_MODEL= NO

# % Damping factor for the engine inflow.
# DAMP_ENGINE_INFLOW= 0.95

# % Damping factor for the engine exhaust.
# DAMP_ENGINE_EXHAUST= 0.95

# % Engine nu factor (SA model).
# ENGINE_NU_FACTOR= 3.0

# % Actuator disk jump definition using ratio or difference (DIFFERENCE, RATIO)
# ACTDISK_JUMP= DIFFERENCE

# % Number of times BC Thrust is updated in a fix Net Thrust problem (5 by default)
# UPDATE_BCTHRUST= 100

# % Initial BC Thrust guess for POWER or D-T driver (4000.0 lbf by default)
# INITIAL_BCTHRUST= 4000.0

# % Initialization with a subsonic flow around the engine.
# SUBSONIC_ENGINE= NO

# % Axis of the cylinder that defines the subsonic region (A_X, A_Y, A_Z, B_X, B_Y, B_Z, Radius)
# SUBSONIC_ENGINE_CYL= ( 0.0, 0.0, 0.0, 1.0, 0.0 , 0.0, 1.0 )

# % Flow variables that define the subsonic region (Mach, Alpha, Beta, Pressure, Temperature)
# SUBSONIC_ENGINE_VALUES= ( 0.4, 0.0, 0.0, 2116.216, 518.67 )

# % ------------------------- TURBOMACHINERY SIMULATION -------------------------%

# % Specify kind of architecture for each zone (AXIAL, CENTRIPETAL, CENTRIFUGAL,
# %                                             CENTRIPETAL_AXIAL, AXIAL_CENTRIFUGAL)
# TURBOMACHINERY_KIND= CENTRIPETAL CENTRIPETAL_AXIAL

# % Specify kind of interpolation for the mixing-plane (LINEAR_INTERPOLATION,
# %                                                     NEAREST_SPAN, MATCHING)
# MIXINGPLANE_INTERFACE_KIND= LINEAR_INTERPOLATION

# % Specify option for turbulent mixing-plane (YES, NO) default NO
# TURBULENT_MIXINGPLANE= YES

# % Specify ramp option for Outlet pressure (YES, NO) default NO
# RAMP_OUTLET_PRESSURE= NO

# % Parameters of the outlet pressure ramp (starting outlet pressure,
# % updating-iteration-frequency, total number of iteration for the ramp)
# RAMP_OUTLET_PRESSURE_COEFF= (400000.0, 10.0, 500)

# % Specify ramp option for rotating frame (YES, NO) default NO
# RAMP_ROTATING_FRAME= YES

# % Parameters of the rotating frame ramp (starting rotational speed,
# % updating-iteration-frequency, total number of iteration for the ramp)
# RAMP_ROTATING_FRAME_COEFF= (0.0, 39.0, 500)

# % Specify Kind of average process for linearizing the Navier-Stokes
# % equation at inflow and outflow BCs included at the mixing-plane interface
# % (ALGEBRAIC, AREA, MASSSFLUX, MIXEDOUT) default AREA
# AVERAGE_PROCESS_KIND= MIXEDOUT

# % Specify Kind of average process for computing turbomachienry performance parameters
# % (ALGEBRAIC, AREA, MASSSFLUX, MIXEDOUT) default AREA
# PERFORMANCE_AVERAGE_PROCESS_KIND= MIXEDOUT

# % Parameters of the Newton method for the MIXEDOUT average algorithm
# % (under relaxation factor, tollerance, max number of iterations)
# MIXEDOUT_COEFF= (1.0, 1.0E-05, 15)

# % Limit of Mach number below which the mixedout algorithm is substituted
# % with a AREA average algorithm to avoid numerical issues
# AVERAGE_MACH_LIMIT= 0.05

# % ------------------- RADIATIVE HEAT TRANSFER SIMULATION ----------------------%

# % Type of radiation model (NONE, P1)
# RADIATION_MODEL = NONE

# % Kind of initialization of the P1 model (ZERO, TEMPERATURE_INIT)
# P1_INITIALIZATION = TEMPERATURE_INIT

# % Absorption coefficient
# ABSORPTION_COEFF = 1.0

# % Scattering coefficient
# SCATTERING_COEFF = 0.0

# % Apply a volumetric heat source as a source term (NO, YES) in the form of an ellipsoid (YES, NO)
# HEAT_SOURCE = NO

# % Value of the volumetric heat source
# HEAT_SOURCE_VAL = 1.0E6

# % Rotation of the volumetric heat source respect to Z axis (degrees)
# HEAT_SOURCE_ROTATION_Z = 0.0

# % Position of heat source center (Heat_Source_Center_X, Heat_Source_Center_Y, Heat_Source_Center_Z)
# HEAT_SOURCE_CENTER = ( 0.0, 0.0, 0.0 )

# % Vector of heat source radii (Heat_Source_Radius_A, Heat_Source_Radius_B, Heat_Source_Radius_C)
# HEAT_SOURCE_RADIUS = ( 1.0, 1.0, 1.0 )

# % Wall emissivity of the marker for radiation purposes
# MARKER_EMISSIVITY = ( MARKER_NAME, 1.0 )

# % Courant-Friedrichs-Lewy condition of the finest grid in radiation solvers
# CFL_NUMBER_RAD = 1.0E3

# % Time discretization for radiation problems (EULER_IMPLICIT)
# TIME_DISCRE_RADIATION = EULER_IMPLICIT

# --------------------- INVERSE DESIGN SIMULATION -----------------------------

# % Evaluate an inverse design problem using Cp (NO, YES)
# INV_DESIGN_CP= NO

# % Evaluate an inverse design problem using heat flux (NO, YES)
# INV_DESIGN_HEATFLUX= NO

# ----------------------- BODY FORCE DEFINITION -------------------------------

# % Apply a body force as a source term (NO, YES)
# BODY_FORCE= NO

# % Vector of body force values (BodyForce_X, BodyForce_Y, BodyForce_Z)
# BODY_FORCE_VECTOR= ( 0.0, 0.0, 0.0 )

# --------------------- STREAMWISE PERIODICITY DEFINITION ---------------------

# % Generally for streamwise periodictiy one has to set MARKER_PERIODIC= (<inlet>, <outlet>, ...)
# % appropriately as a boundary condition.
# %
# % Specify type of streamwise periodictiy (default=NONE, PRESSURE_DROP, MASSFLOW)
# KIND_STREAMWISE_PERIODIC= NONE

# % Delta P [Pa] value that drives the flow as a source term in the momentum equations.
# % Defaults to 1.0.
# STREAMWISE_PERIODIC_PRESSURE_DROP= 1.0

# % Target massflow [kg/s]. Necessary pressure drop is determined iteratively. 
# % Initial value is given via STREAMWISE_PERIODIC_PRESSURE_DROP. Default value 1.0.
# % Use INC_OUTLET_DAMPING as a relaxation factor. Default value 0.1 is a good start.
# STREAMWISE_PERIODIC_MASSFLOW= 0.0

# % Use streamwise periodic temperature (default=NO, YES)
# % If NO, the heatflux is taken out at the outlet.
# % This option is only necessary if INC_ENERGY_EQUATION=YES
# STREAMWISE_PERIODIC_TEMPERATURE= NO

# % Prescribe integrated heat [W] extracted at the periodic "outlet".
# % Only active if STREAMWISE_PERIODIC_TEMPERATURE= NO.
# % If set to zero, the heat is integrated automatically over all present MARKER_HEATFLUX.
# % Upon convergence, the area averaged inlet temperature will be INC_TEMPERATURE_INIT.
# % Defaults to 0.0.
# STREAMWISE_PERIODIC_OUTLET_HEAT= 0.0

# -------------------- BOUNDARY CONDITION DEFINITION --------------------------

from . import boundary_condition

# % ------------------------ WALL ROUGHNESS DEFINITION --------------------------%
# % The equivalent sand grain roughness height (k_s) on each of the wall. This must be in m.
# % This is a list of (string, double) each element corresponding to the MARKER defined in WALL_TYPE.
# WALL_ROUGHNESS = (wall1, ks1, wall2, ks2)
# %WALL_ROUGHNESS = (wall1, ks1, wall2, 0.0) %is also allowed

# % ------------------------ WALL FUNCTION DEFINITION --------------------------%
# %
# % The von Karman constant, the constant below only affects the standard wall function model 
# WALLMODEL_KAPPA= 0.41
# %
# % The wall function model constant B 
# WALLMODEL_B= 5.5
# %
# % The y+ value below which the wall function is switched off and we resolve the wall 
# WALLMODEL_MINYPLUS= 5.0
# %
# % [Expert] Max Newton iterations used for the standard wall function
# WALLMODEL_MAXITER= 200
# %
# % [Expert] relaxation factor for the Newton iterations of the standard wall function 
# WALLMODEL_RELFAC= 0.5

# ------------------------ SURFACES IDENTIFICATION ----------------------------

from . import surfaces

# ------------- COMMON PARAMETERS DEFINING THE NUMERICAL METHOD ---------------

from . import common

# ----------- SLOPE LIMITER AND DISSIPATION SENSOR DEFINITION -----------------

from . import limiter

# ------------------------ LINEAR SOLVER DEFINITION ---------------------------

from . import linear_solver

# -------------------------- MULTIGRID PARAMETERS -----------------------------

from . import multigrid

# -------------------- FLOW NUMERICAL METHOD DEFINITION -----------------------

from . import flow_numerical

# ------------------- FEM FLOW NUMERICAL METHOD DEFINITION --------------------
# %
# % FEM numerical method (DG)
# NUM_METHOD_FEM_FLOW= DG
# %
# % Riemann solver used for DG (ROE, LAX-FRIEDRICH, AUSM, AUSMPW+, HLLC, VAN_LEER)
# RIEMANN_SOLVER_FEM= ROE
# %
# % Constant factor applied for quadrature with straight elements (2.0 by default)
# QUADRATURE_FACTOR_STRAIGHT_FEM = 2.0
# %
# % Constant factor applied for quadrature with curved elements (3.0 by default)
# QUADRATURE_FACTOR_CURVED_FEM = 3.0
# %
# % Factor for the symmetrizing terms in the DG FEM discretization (1.0 by default)
# THETA_INTERIOR_PENALTY_DG_FEM = 1.0
# %
# % Compute the entropy in the fluid model (YES, NO)
# COMPUTE_ENTROPY_FLUID_MODEL= YES
# %
# % Use the lumped mass matrix for steady DGFEM computations (NO, YES)
# USE_LUMPED_MASSMATRIX_DGFEM= NO
# %
# % Only compute the exact Jacobian of the spatial discretization (NO, YES)
# JACOBIAN_SPATIAL_DISCRETIZATION_ONLY= NO
# %
# % Number of aligned bytes for the matrix multiplications. Multiple of 64. (128 by default)
# ALIGNED_BYTES_MATMUL= 128
# %
# % Time discretization (RUNGE-KUTTA_EXPLICIT, CLASSICAL_RK4_EXPLICIT, ADER_DG)
# TIME_DISCRE_FEM_FLOW= RUNGE-KUTTA_EXPLICIT
# %
# % Number of time DOFs for the predictor step of ADER-DG (2 by default)
# %TIME_DOFS_ADER_DG= 2
# % Factor applied during quadrature in time for ADER-DG. (2.0 by default)
# %QUADRATURE_FACTOR_TIME_ADER_DG = 2.0
# %
# % Type of discretization used in the predictor step of ADER-DG (ADER_ALIASED_PREDICTOR, ADER_NON_ALIASED_PREDICTOR)
# ADER_PREDICTOR= ADER_ALIASED_PREDICTOR
# % Number of time levels for time accurate local time stepping. (1 by default, max. allowed 15)
# LEVELS_TIME_ACCURATE_LTS= 1
# %
# % Specify the method for matrix coloring for Jacobian computations (GREEDY_COLORING, NATURAL_COLORING)
# KIND_MATRIX_COLORING= GREEDY_COLORING

# % -------------------- TURBULENT NUMERICAL METHOD DEFINITION ------------------%
# %
# % Convective numerical method (SCALAR_UPWIND)
# CONV_NUM_METHOD_TURB= SCALAR_UPWIND
# %
# % Time discretization (EULER_IMPLICIT)
# TIME_DISCRE_TURB= EULER_IMPLICIT
# %
# % Reduction factor of the CFL coefficient in the turbulence problem
# CFL_REDUCTION_TURB= 1.0

# % --------------------- HEAT NUMERICAL METHOD DEFINITION ----------------------%
# %
# % Value of the thermal diffusivity
# THERMAL_DIFFUSIVITY= 1.0
# %
# % Convective numerical method
# CONV_NUM_METHOD_HEAT= SPACE_CENTERED
# %
# % Check if the MUSCL scheme should be used
# MUSCL_HEAT= YES
# %
# % 2nd and 4th order artificial dissipation coefficients for the JST method
# JST_SENSOR_COEFF_HEAT= ( 0.5, 0.15 )
# %
# % Time discretization
# TIME_DISCRE_HEAT= EULER_IMPLICIT
# %
# % ---------------- ADJOINT-FLOW NUMERICAL METHOD DEFINITION -------------------%
# %
# % Frozen the slope limiter in the discrete adjoint formulation (NO, YES)
# FROZEN_LIMITER_DISC= NO
# %
# % Frozen the turbulent viscosity in the discrete adjoint formulation (NO, YES)
# FROZEN_VISC_DISC= NO
# %
# % Use an inconsistent spatial integration (primal-dual) in the discrete
# % adjoint formulation. The AD will use the numerical methods in
# % the ADJOINT-FLOW NUMERICAL METHOD DEFINITION section (NO, YES)
# INCONSISTENT_DISC= NO
# %
# % Convective numerical method (JST, LAX-FRIEDRICH, ROE)
# CONV_NUM_METHOD_ADJFLOW= JST
# %
# % Time discretization (RUNGE-KUTTA_EXPLICIT, EULER_IMPLICIT)
# TIME_DISCRE_ADJFLOW= EULER_IMPLICIT
# %
# % Relaxation coefficient (also for discrete adjoint problems)
# RELAXATION_FACTOR_ADJOINT= 1.0
# %
# % Enable (if != 0) quasi-Newton acceleration/stabilization of discrete adjoints
# QUASI_NEWTON_NUM_SAMPLES= 20
# %
# % Reduction factor of the CFL coefficient in the adjoint problem
# CFL_REDUCTION_ADJFLOW= 0.8
# %
# % Limit value for the adjoint variable
# LIMIT_ADJFLOW= 1E6
# %
# % Use multigrid in the adjoint problem (NO, YES)
# MG_ADJFLOW= YES

# % ---------------- ADJOINT-TURBULENT NUMERICAL METHOD DEFINITION --------------%
# %
# % Convective numerical method (SCALAR_UPWIND)
# CONV_NUM_METHOD_ADJTURB= SCALAR_UPWIND
# %
# % Time discretization (EULER_IMPLICIT)
# TIME_DISCRE_ADJTURB= EULER_IMPLICIT
# %
# % Reduction factor of the CFL coefficient in the adjoint turbulent problem
# CFL_REDUCTION_ADJTURB= 0.01


# % -------------------- NEMO NUMERICAL METHOD DEFINITION -----------------------%
# %
# % Mixture transport properties (WILKE,GUPTA-YOS,CHAPMANN-ENSKOG)
# TRANSPORT_COEFF_MODEL = WILKE

# % ----------------------- GEOMETRY EVALUATION PARAMETERS ----------------------%
# %
# % Marker(s) of the surface where geometrical based function will be evaluated
# GEO_MARKER= ( airfoil )
# %
# % Description of the geometry to be analyzed (AIRFOIL, WING)
# GEO_DESCRIPTION= AIRFOIL
# %
# % Coordinate of the stations to be analyzed
# GEO_LOCATION_STATIONS= (0.0, 0.5, 1.0)
# %
# % Geometrical bounds (Y coordinate) for the wing geometry analysis or
# % fuselage evaluation (X coordinate)
# GEO_BOUNDS= (1.5, 3.5)
# %
# % Plot loads and Cp distributions on each airfoil section
# GEO_PLOT_STATIONS= NO
# %
# % Number of section cuts to make when calculating wing geometry
# GEO_NUMBER_STATIONS= 25
# %
# % Geometrical evaluation mode (FUNCTION, GRADIENT)
# GEO_MODE= FUNCTION

# % ------------------------- GRID ADAPTATION STRATEGY --------------------------%
# %
# % Kind of grid adaptation (NONE, PERIODIC, FULL, FULL_FLOW, GRAD_FLOW,
# %                          FULL_ADJOINT, GRAD_ADJOINT, GRAD_FLOW_ADJ, ROBUST,
# %                          FULL_LINEAR, COMPUTABLE, COMPUTABLE_ROBUST,
# %                          REMAINING, WAKE, SMOOTHING, SUPERSONIC_SHOCK)
# KIND_ADAPT= FULL_FLOW
# %
# % Percentage of new elements (% of the original number of elements)
# NEW_ELEMS= 5
# %
# % Scale factor for the dual volume
# DUALVOL_POWER= 0.5
# %
# % Adapt the boundary elements (NO, YES)
# ADAPT_BOUNDARY= YES

# % ----------------------- DESIGN VARIABLE PARAMETERS --------------------------%
# %
# % Kind of deformation (NO_DEFORMATION, SCALE_GRID, TRANSLATE_GRID, ROTATE_GRID,
# %                      FFD_SETTING, FFD_NACELLE,
# %                      FFD_CONTROL_POINT, FFD_CAMBER, FFD_THICKNESS, FFD_TWIST
# %                      FFD_CONTROL_POINT_2D, FFD_CAMBER_2D, FFD_THICKNESS_2D,
# %                      FFD_TWIST_2D, HICKS_HENNE, SURFACE_BUMP, SURFACE_FILE)
# DV_KIND= FFD_SETTING
# %
# % Marker of the surface in which we are going apply the shape deformation
# DV_MARKER= ( airfoil )
# %
# % Parameters of the shape deformation
# % - NO_DEFORMATION ( 1.0 )
# % - TRANSLATE_GRID ( x_Disp, y_Disp, z_Disp ), as a unit vector
# % - ROTATE_GRID ( x_Orig, y_Orig, z_Orig, x_End, y_End, z_End ) axis, DV_VALUE in deg.
# % - SCALE_GRID ( 1.0 )
# % - ANGLE_OF_ATTACK ( 1.0 )
# % - FFD_SETTING ( 1.0 )
# % - FFD_CONTROL_POINT ( FFD_BoxTag, i_Ind, j_Ind, k_Ind, x_Disp, y_Disp, z_Disp )
# % - FFD_NACELLE ( FFD_BoxTag, rho_Ind, theta_Ind, phi_Ind, rho_Disp, phi_Disp )
# % - FFD_GULL ( FFD_BoxTag, j_Ind )
# % - FFD_ANGLE_OF_ATTACK ( FFD_BoxTag, 1.0 )
# % - FFD_CAMBER ( FFD_BoxTag, i_Ind, j_Ind )
# % - FFD_THICKNESS ( FFD_BoxTag, i_Ind, j_Ind )
# % - FFD_TWIST ( FFD_BoxTag, j_Ind, x_Orig, y_Orig, z_Orig, x_End, y_End, z_End )
# % - FFD_CONTROL_POINT_2D ( FFD_BoxTag, i_Ind, j_Ind, x_Disp, y_Disp )
# % - FFD_CAMBER_2D ( FFD_BoxTag, i_Ind )
# % - FFD_THICKNESS_2D ( FFD_BoxTag, i_Ind )
# % - FFD_TWIST_2D ( FFD_BoxTag, x_Orig, y_Orig )
# % - HICKS_HENNE ( Lower Surface (0)/Upper Surface (1)/Only one Surface (2), x_Loc )
# % - SURFACE_BUMP ( x_Start, x_End, x_Loc )
# DV_PARAM= ( 1, 0.5 )
# %
# % Value of the shape deformation
# DV_VALUE= 0.01
# %
# % For DV_KIND = SURFACE_FILE: With SU2_DEF, give filename for surface
# % deformation prescribed by an external parameterization. List moving markers
# % in DV_MARKER and provide an ASCII file with name specified with DV_FILENAME
# % and with format:
# % GlobalID_0, x_0, y_0, z_0
# % GlobalID_1, x_1, y_1, z_1
# %   ...
# % GlobalID_N, x_N, y_N, z_N
# % where N is the total number of vertices on all moving markers, and x/y/z are
# % the new position of each vertex. Points can be in any order. When SU2_DOT
# % is called in SURFACE_FILE mode, sensitivities on surfaces will be written
# % to an ASCII file with name given by DV_SENS_FILENAME and with format as
# % rows of x, y, z, dJ/dx, dJ/dy, dJ/dz for each surface vertex.
# DV_FILENAME= surface_positions.dat
# DV_SENS_FILENAME= surface_sensitivity.dat
# %
# % Format for volume sensitivity file read by SU2_DOT (SU2_NATIVE,
# % UNORDERED_ASCII). SU2_NATIVE is the native SU2 restart file (default),
# % while UNORDERED_ASCII provide a file of field sensitivities
# % as an ASCII file with name given by DV_SENS_FILENAMEand with format as
# % rows of x, y, z, dJ/dx, dJ/dy, dJ/dz for each grid point.
# DV_SENSITIVITY_FORMAT= SU2_NATIVE
# DV_UNORDERED_SENS_FILENAME= unordered_sensitivity.dat

# % ---------------- MESH DEFORMATION PARAMETERS (NEW SOLVER) -------------------%
# %
# % Use the reformatted pseudo-elastic solver for grid deformation
# DEFORM_MESH= YES
# %
# % Moving markers which deform the mesh
# MARKER_DEFORM_MESH = ( airfoil )
# MARKER_DEFORM_MESH_SYM_PLANE = ( wall )

# % ------------------------ GRID DEFORMATION PARAMETERS ------------------------%
# %
# % Linear solver or smoother for implicit formulations (FGMRES, RESTARTED_FGMRES, BCGSTAB)
# DEFORM_LINEAR_SOLVER= FGMRES
# %
# % Preconditioner of the Krylov linear solver (ILU, LU_SGS, JACOBI)
# DEFORM_LINEAR_SOLVER_PREC= ILU
# %
# % Number of smoothing iterations for mesh deformation
# DEFORM_LINEAR_SOLVER_ITER= 1000
# %
# % Number of nonlinear deformation iterations (surface deformation increments)
# DEFORM_NONLINEAR_ITER= 1
# %
# % Minimum residual criteria for the linear solver convergence of grid deformation
# DEFORM_LINEAR_SOLVER_ERROR= 1E-14
# %
# % Print the residuals during mesh deformation to the console (YES, NO)
# DEFORM_CONSOLE_OUTPUT= YES
# %
# % Deformation coefficient (linear elasticity limits from -1.0 to 0.5, a larger
# % value is also possible)
# DEFORM_COEFF = 1E6
# %
# % Type of element stiffness imposed for FEA mesh deformation (INVERSE_VOLUME,
# %                                           WALL_DISTANCE, CONSTANT_STIFFNESS)
# DEFORM_STIFFNESS_TYPE= WALL_DISTANCE
# %
# % Deform the grid only close to the surface. It is possible to specify how much
# % of the volumetric grid is going to be deformed in meters or inches (1E6 by default)
# DEFORM_LIMIT = 1E6

# % -------------------- FREE-FORM DEFORMATION PARAMETERS -----------------------%
# %
# % Tolerance of the Free-Form Deformation point inversion
# FFD_TOLERANCE= 1E-10
# %
# % Maximum number of iterations in the Free-Form Deformation point inversion
# FFD_ITERATIONS= 500

# % Parameters for prevention of self-intersections within FFD box
# FFD_INTPREV = YES
# FFD_INTPREV_ITER = 10
# FFD_INTPREV_DEPTH = 3

# % Parameters for prevention of nonconvex elements in mesh after deformation
# CONVEXITY_CHECK = YES
# CONVEXITY_CHECK_ITER = 10
# CONVEXITY_CHECK_DEPTH = 3

# %
# % FFD box definition: 3D case (FFD_BoxTag, X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3, X4, Y4, Z4,
# %                              X5, Y5, Z5, X6, Y6, Z6, X7, Y7, Z7, X8, Y8, Z8)
# %                     2D case (FFD_BoxTag, X1, Y1, 0.0, X2, Y2, 0.0, X3, Y3, 0.0, X4, Y4, 0.0,
# %                              0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
# FFD_DEFINITION= (MAIN_BOX, 0.5, 0.25, -0.25, 1.5, 0.25, -0.25, 1.5, 0.75, -0.25, 0.5, 0.75, -0.25, 0.5, 0.25, 0.25, 1.5, 0.25, 0.25, 1.5, 0.75, 0.25, 0.5, 0.75, 0.25)
# %
# % FFD box degree: 3D case (x_degree, y_degree, z_degree)
# %                 2D case (x_degree, y_degree, 0)
# FFD_DEGREE= (10, 10, 1)
# %
# % Surface grid continuity at the intersection with the faces of the FFD boxes.
# % To keep a particular level of surface continuity, SU2 automatically freezes the right
# % number of control point planes (NO_DERIVATIVE, 1ST_DERIVATIVE, 2ND_DERIVATIVE, USER_INPUT)
# FFD_CONTINUITY= 2ND_DERIVATIVE
# %
# % Definition of the FFD planes to be frozen in the FFD (x,y,z).
# % Value from 0 FFD degree in that direction. Pick a value larger than degree if you don't want to fix any plane.
# FFD_FIX_I= (0,2,3)
# FFD_FIX_J= (0,2,3)
# FFD_FIX_K= (0,2,3)
# %
# % There is a symmetry plane (j=0) for all the FFD boxes (YES, NO)
# FFD_SYMMETRY_PLANE= NO
# %
# % FFD coordinate system (CARTESIAN)
# FFD_COORD_SYSTEM= CARTESIAN
# %
# % Vector from the cartesian axis the cylindrical or spherical axis (using cartesian coordinates)
# % Note that the location of the axis will affect the wall curvature of the FFD box as well as the
# % design variable effect.
# FFD_AXIS= (0.0, 0.0, 0.0)
# %
# % FFD Blending function: Bezier curves with global support (BEZIER), uniform BSplines with local support (BSPLINE_UNIFORM)
# FFD_BLENDING= BEZIER
# %
# % Order of the BSplines
# FFD_BSPLINE_ORDER= 2, 2, 2
# %
# % ------------------- UNCERTAINTY QUANTIFICATION DEFINITION -------------------%
# %
# % Using uncertainty quantification module (YES, NO). Only available with SST
# USING_UQ= NO
# %
# % Eigenvalue perturbation definition (1, 2, or 3)
# UQ_COMPONENT= 1
# %
# % Permuting eigenvectors (YES, NO)
# UQ_PERMUTE= NO
# %
# % Under-relaxation factor (float [0,1], default = 0.1)
# UQ_URLX= 0.1
# %
# % Perturbation magnitude (float [0,1], default= 1.0)
# UQ_DELTA_B= 1.0
# %
# % --------------------- HYBRID PARALLEL (MPI+OpenMP) OPTIONS ---------------------%
# %
# % An advanced performance parameter for FVM solvers, a large-ish value should be best
# % when relatively few threads per MPI rank are in use (~4). However, maximum parallelism
# % is obtained with EDGE_COLORING_GROUP_SIZE=1, consider using this value only if SU2
# % warns about low coloring efficiency during preprocessing (performance is usually worse).
# % Setting the option to 0 disables coloring and a different strategy is used instead,
# % that strategy is automatically used when the coloring efficiency is less than 0.875.
# % The optimum value/strategy is case-dependent.
# EDGE_COLORING_GROUP_SIZE= 512
# %
# % Independent "threads per MPI rank" setting for LU-SGS and ILU preconditioners.
# % For problems where time is spend mostly in the solution of linear systems (e.g. elasticity,
# % very high CFL central schemes), AND, if the memory bandwidth of the machine is saturated
# % (4 or more cores per memory channel) better performance (via a reduction in linear iterations)
# % may be possible by using a smaller value than that defined by the system or in the call to
# % SU2_CFD (via the -t/--threads option).
# % The default (0) means "same number of threads as for all else".
# LINEAR_SOLVER_PREC_THREADS= 0
# %
# % ----------------------- PARTITIONING OPTIONS (ParMETIS) ------------------------ %
# %
# % Load balancing tolerance, lower values will make ParMETIS work harder to evenly
# % distribute the work-estimate metric across all MPI ranks, at the expense of more
# % edge cuts (i.e. increased communication cost).
# PARMETIS_TOLERANCE= 0.02
# %
# % The work-estimate metric is a weighted function of the work-per-edge (e.g. spatial
# % discretization, linear system solution) and of the work-per-point (e.g. source terms,
# % temporal discretization) the former usually accounts for >90% of the total.
# % These weights are INTEGERS (for compatibility with ParMETIS) thus not [0, 1].
# % To balance memory usage (instead of computation) the point weight needs to be
# % increased (especially for explicit time integration methods).
# PARMETIS_EDGE_WEIGHT= 1
# PARMETIS_POINT_WEIGHT= 0
# %
# % ------------------------- SCREEN/HISTORY VOLUME OUTPUT --------------------------%

SCREEN_OUTPUT = SU2ConfigField(
    "SCREEN_OUTPUT", ("INNER_ITER", "RMS_DENSITY", "RMS_MOMENTUM-X", "RMS_MOMENTUM-Y", "RMS_ENERGY"),
    "Screen output fields (use 'SU2_CFD -d <config_file>' to view list of available fields).")

# % History output groups (use 'SU2_CFD -d <config_file>' to view list of available fields)
# HISTORY_OUTPUT= (ITER, RMS_RES)

# % Volume output fields/groups (use 'SU2_CFD -d <config_file>' to view list of available fields)
# VOLUME_OUTPUT= (COORDINATES, SOLUTION, PRIMITIVE)

# % Writing frequency for screen output
# SCREEN_WRT_FREQ_INNER= 1
# SCREEN_WRT_FREQ_OUTER= 1
# SCREEN_WRT_FREQ_TIME= 1

# % Writing frequency for history output
# HISTORY_WRT_FREQ_INNER= 1
# HISTORY_WRT_FREQ_OUTER= 1
# HISTORY_WRT_FREQ_TIME= 1

# % Writing frequency for volume/surface output
# OUTPUT_WRT_FREQ= 10

# ------------------------- INPUT/OUTPUT FILE INFORMATION --------------------------

from . import file_io

# % --------------------- OPTIMAL SHAPE DESIGN DEFINITION -----------------------%
# %
# % Available flow based objective functions or constraint functions
# %    DRAG, LIFT, SIDEFORCE, EFFICIENCY, BUFFET,
# %    FORCE_X, FORCE_Y, FORCE_Z,
# %    MOMENT_X, MOMENT_Y, MOMENT_Z,
# %    THRUST, TORQUE, FIGURE_OF_MERIT,
# %    EQUIVALENT_AREA, NEARFIELD_PRESSURE,
# %    TOTAL_HEATFLUX, MAXIMUM_HEATFLUX,
# %    INVERSE_DESIGN_PRESSURE, INVERSE_DESIGN_HEATFLUX,
# %    SURFACE_TOTAL_PRESSURE, SURFACE_MASSFLOW
# %    SURFACE_STATIC_PRESSURE, SURFACE_MACH
# %
# % Available geometrical based objective functions or constraint functions
# %    AIRFOIL_AREA, AIRFOIL_THICKNESS, AIRFOIL_CHORD, AIRFOIL_TOC, AIRFOIL_AOA,
# %    WING_VOLUME, WING_MIN_THICKNESS, WING_MAX_THICKNESS, WING_MAX_CHORD, WING_MIN_TOC, WING_MAX_TWIST, WING_MAX_CURVATURE, WING_MAX_DIHEDRAL
# %    STATION#_WIDTH, STATION#_AREA, STATION#_THICKNESS, STATION#_CHORD, STATION#_TOC,
# %    STATION#_TWIST (where # is the index of the station defined in GEO_LOCATION_STATIONS)
# %
# % Available design variables
# % 2D Design variables
# %    FFD_CONTROL_POINT_2D   (  19, Scale | Mark. List | FFD_BoxTag, i_Ind, j_Ind, x_Mov, y_Mov )
# %    FFD_CAMBER_2D          (  20, Scale | Mark. List | FFD_BoxTag, i_Ind )
# %    FFD_THICKNESS_2D       (  21, Scale | Mark. List | FFD_BoxTag, i_Ind )
# %    FFD_TWIST_2D           (  22, Scale | Mark. List | FFD_BoxTag, x_Orig, y_Orig )
# %    HICKS_HENNE            (  30, Scale | Mark. List | Lower(0)/Upper(1) side, x_Loc )
# %    ANGLE_OF_ATTACK        ( 101, Scale | Mark. List | 1.0 )
# %
# % 3D Design variables
# %    FFD_CONTROL_POINT      (  11, Scale | Mark. List | FFD_BoxTag, i_Ind, j_Ind, k_Ind, x_Mov, y_Mov, z_Mov )
# %    FFD_NACELLE            (  12, Scale | Mark. List | FFD_BoxTag, rho_Ind, theta_Ind, phi_Ind, rho_Mov, phi_Mov )
# %    FFD_GULL               (  13, Scale | Mark. List | FFD_BoxTag, j_Ind )
# %    FFD_CAMBER             (  14, Scale | Mark. List | FFD_BoxTag, i_Ind, j_Ind )
# %    FFD_TWIST              (  15, Scale | Mark. List | FFD_BoxTag, j_Ind, x_Orig, y_Orig, z_Orig, x_End, y_End, z_End )
# %    FFD_THICKNESS          (  16, Scale | Mark. List | FFD_BoxTag, i_Ind, j_Ind )
# %    FFD_ROTATION           (  18, Scale | Mark. List | FFD_BoxTag, x_Axis, y_Axis, z_Axis, x_Turn, y_Turn, z_Turn )
# %    FFD_ANGLE_OF_ATTACK    (  24, Scale | Mark. List | FFD_BoxTag, 1.0 )
# %
# % Global design variables
# %    TRANSLATION            (   1, Scale | Mark. List | x_Disp, y_Disp, z_Disp )
# %    ROTATION               (   2, Scale | Mark. List | x_Axis, y_Axis, z_Axis, x_Turn, y_Turn, z_Turn )
# %
# % Definition of multipoint design problems, this option should be combined with the
# % the prefix MULTIPOINT in the objective function or constraint (e.g. MULTIPOINT_DRAG, MULTIPOINT_LIFT, etc.)
# MULTIPOINT_MACH_NUMBER= (0.79, 0.8, 0.81)
# MULTIPOINT_AOA= (1.25, 1.25, 1.25)
# MULTIPOINT_SIDESLIP_ANGLE= (0.0, 0.0, 0.0)
# MULTIPOINT_TARGET_CL= (0.8, 0.8, 0.8)
# MULTIPOINT_REYNOLDS_NUMBER= (1E6, 1E6, 1E6)
# MULTIPOINT_FREESTREAM_PRESSURE= (101325.0, 101325.0, 101325.0)
# MULTIPOINT_FREESTREAM_TEMPERATURE= (288.15, 288.15, 288.15)
# MULTIPOINT_OUTLET_VALUE= (0.0, 0.0, 0.0)
# MULTIPOINT_WEIGHT= (0.33333, 0.33333, 0.33333)
# MULTIPOINT_MESH_FILENAME= (mesh_NACA0012_m79.su2, mesh_NACA0012_m8.su2, mesh_NACA0012_m81.su2)
# %
# % Optimization objective function with scaling factor, separated by semicolons.
# % To include quadratic penalty function: use OPT_CONSTRAINT option syntax within the OPT_OBJECTIVE list.
# % ex= Objective * Scale
# OPT_OBJECTIVE= DRAG
# %
# % Optimization constraint functions with pushing factors (affects its value, not the gradient  in the python scripts), separated by semicolons
# % ex= (Objective = Value ) * Scale, use '>','<','='
# OPT_CONSTRAINT= ( LIFT > 0.328188 ) * 0.001; ( MOMENT_Z > 0.034068 ) * 0.001; ( AIRFOIL_THICKNESS > 0.11 ) * 0.001
# %
# % Factor to reduce the norm of the gradient (affects the objective function and gradient in the python scripts)
# % In general, a norm of the gradient ~1E-6 is desired.
# OPT_GRADIENT_FACTOR= 1E-6
# %
# % Factor to relax or accelerate the optimizer convergence (affects the line search in SU2_DEF)
# % In general, surface deformations of 0.01'' or 0.0001m are desirable
# OPT_RELAX_FACTOR= 1E3
# %
# % Maximum number of iterations
# OPT_ITERATIONS= 100
# %
# % Requested accuracy
# OPT_ACCURACY= 1E-10
# %
# % Optimization bound (bounds the line search in SU2_DEF)
# OPT_LINE_SEARCH_BOUND= 1E6
# %
# % Upper bound for each design variable (bound in the python optimizer)
# OPT_BOUND_UPPER= 1E10
# %
# % Lower bound for each design variable (bound in the python optimizer)
# OPT_BOUND_LOWER= -1E10
# %
# % Finite difference step size for python scripts (0.001 default, recommended
# %                                                 0.001 x REF_LENGTH)
# FIN_DIFF_STEP = 0.001
# %
# % Optimization design variables, separated by semicolons
# DEFINITION_DV= ( 1, 1.0 | airfoil | 0, 0.05 ); ( 1, 1.0 | airfoil | 0, 0.10 ); ( 1, 1.0 | airfoil | 0, 0.15 ); ( 1, 1.0 | airfoil | 0, 0.20 ); ( 1, 1.0 | airfoil | 0, 0.25 ); ( 1, 1.0 | airfoil | 0, 0.30 ); ( 1, 1.0 | airfoil | 0, 0.35 ); ( 1, 1.0 | airfoil | 0, 0.40 ); ( 1, 1.0 | airfoil | 0, 0.45 ); ( 1, 1.0 | airfoil | 0, 0.50 ); ( 1, 1.0 | airfoil | 0, 0.55 ); ( 1, 1.0 | airfoil | 0, 0.60 ); ( 1, 1.0 | airfoil | 0, 0.65 ); ( 1, 1.0 | airfoil | 0, 0.70 ); ( 1, 1.0 | airfoil | 0, 0.75 ); ( 1, 1.0 | airfoil | 0, 0.80 ); ( 1, 1.0 | airfoil | 0, 0.85 ); ( 1, 1.0 | airfoil | 0, 0.90 ); ( 1, 1.0 | airfoil | 0, 0.95 ); ( 1, 1.0 | airfoil | 1, 0.05 ); ( 1, 1.0 | airfoil | 1, 0.10 ); ( 1, 1.0 | airfoil | 1, 0.15 ); ( 1, 1.0 | airfoil | 1, 0.20 ); ( 1, 1.0 | airfoil | 1, 0.25 ); ( 1, 1.0 | airfoil | 1, 0.30 ); ( 1, 1.0 | airfoil | 1, 0.35 ); ( 1, 1.0 | airfoil | 1, 0.40 ); ( 1, 1.0 | airfoil | 1, 0.45 ); ( 1, 1.0 | airfoil | 1, 0.50 ); ( 1, 1.0 | airfoil | 1, 0.55 ); ( 1, 1.0 | airfoil | 1, 0.60 ); ( 1, 1.0 | airfoil | 1, 0.65 ); ( 1, 1.0 | airfoil | 1, 0.70 ); ( 1, 1.0 | airfoil | 1, 0.75 ); ( 1, 1.0 | airfoil | 1, 0.80 ); ( 1, 1.0 | airfoil | 1, 0.85 ); ( 1, 1.0 | airfoil | 1, 0.90 ); ( 1, 1.0 | airfoil | 1, 0.95 )
# %
# % Use combined objective within gradient evaluation: may reduce cost to compute gradients when using the adjoint formulation.
# OPT_COMBINE_OBJECTIVE = NO

# --------------------- LIBROM PARAMETERS -----------------------
# % LibROM can be found here: https://github.com/LLNL/libROM

# % Toggle saving to librom (NO, YES)
# SAVE_LIBROM = NO

# % Prefix to the saved libROM files (default: su2)
# LIBROM_BASE_FILENAME = su2

# % Specify POD basis generation algorithm (STATIC_POD, INCREMENTAL_POD) 
# % STATIC_POD recommended for steady problems
# BASIS_GENERATION = STATIC_POD

# % Maximum number of basis vectors to keep (default: 100)
# MAX_BASIS_DIM = 100
