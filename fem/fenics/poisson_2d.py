# -*- coding: utf-8 -*-
from dolfin import Point
from dolfin import RectangleMesh
from dolfin import FunctionSpace
from dolfin import DirichletBC
from dolfin import TrialFunction
from dolfin import TestFunction
from dolfin import Function
from dolfin import dot
from dolfin import grad
from dolfin import dx
from dolfin import solve
from fenix import VtkFileWriter

# Define discretization and domain.
nxy = 10
xy0 = Point(-1, -1)
xy1 = Point(1, 1)

# Define source term of `laplacian(u) = f`.
f = 1.0

# Create a 2D grid from `xy0` to `xy1`.
mesh = RectangleMesh(xy0, xy1, nxy, nxy)

# Define a function space of polynomials of order 2.
V = FunctionSpace(mesh, "P", 2)

# Create a fixed boundary condition on borders.
bc = DirichletBC(V, 0, "on_boundary")

# Create trial and test functions over space `V`.
u = TrialFunction(V)
v = TestFunction(V)

# Declare problem LHS.
a = dot(grad(u), grad(v)) * dx

# Declare problem RHS.
L = f * v * dx

# Replace the symbolic u by the solution form.
u = Function(V)

# Call solver.
solve(a == L, u, bc)

# Dump results to file.
with VtkFileWriter("poisson_2d.pvd") as fp:
    fp.write(u)
