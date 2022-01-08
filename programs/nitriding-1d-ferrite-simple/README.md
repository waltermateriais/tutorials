# rust-nitriding

Solution of diffusion equation in Rust

## Build

The recommended way to build it is by using a Docker container for which a Dockerfile is already provided with the full environment for development. This project has no external Rust dependencies (crates). To run it simply execute `cargo run` or `cargo run --release`. Output should be something like this:

```
*** NITRIDING MASS INTAKE MODEL ***


* Using B.C. DirichletDirichlet
* The following concerns the full exposed length
* Mass intake by material 3.24 kg/h
* Simulation took is: 190.921184ms


* Using B.C. DirichletSymmetry
* The following concerns the full exposed length
* Mass intake by material 3.24 kg/h
* Simulation took is: 112.42829ms


*** NITRIDING MASS INTAKE MODEL ***
```

Please notice that currently there is no parser for inputs. If you need to simulate with other conditions consider editing `main`, the inputs are reasoably documented with comments for now.

## To-do

- [ ] Implement final state plotting.
- [ ] Implement parameter parsing from input file (JSON/YAML,...).
- [ ] Provide phase transformation (BCC > FCC) during process.
- [ ] Create a library with reusable code for diffusion.
- [ ] Provide a 2-D solver.
- [ ] [Implement Python API](https://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-python-using-pyo3/)
