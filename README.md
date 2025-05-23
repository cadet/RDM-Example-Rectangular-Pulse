# Rectangular Pulse Elution Simulation with CADET

This repository contains an example simulation of the elution of a rectangular pulse using **CADET-Process** and **CADET-RDM**. Here, a **General Rate Model (GRM)** with a **linear binding model** is used to examine the influence of **dispersion** on the elution behavior.

This example reproduces part of the case study from:

* *"Analytical solutions and moment analysis of general rate model for linear liquid chromatography"*
  Shamsul Qamar, Javeria Nawaz Abbasi, Shumaila Javeed, Andreas Seidel-Morgenstern
  *Chemical Engineering Science* (2014); 107:192–205
  [https://doi.org/10.1016/j.ces.2013.12.019](https://doi.org/10.1016/j.ces.2013.12.019)

It is also referenced in:

* *"Chromatography Analysis and Design Toolkit (CADET)"*
  Samuel Leweke, Eric von Lieres
  *Computers & Chemical Engineering* (2018); 113:274–294
  [https://doi.org/10.1016/j.compchemeng.2018.02.025](https://doi.org/10.1016/j.compchemeng.2018.02.025)

---

## Authors

* Katharina Paul
* Ronald Jäpel
* Hannah Lanzrath

---

## Running the Example Simulation

1. Clone this repository.
2. Set up the environment using the `environment.yml` file.
3. Run the simulation:

   ```bash
   python main.py
   ```

The results will be stored in the `src` folder inside the `output` directory.

> **Note**: Running `cadet-rdm` requires [**Git LFS**](https://git-lfs.com/), which needs to be installed separately.
>
> * **Ubuntu/Debian**:
>
>   ```bash
>   sudo apt-get install git-lfs
>   git lfs install
>   ```
>
> * **macOS** (with Homebrew):
>
>   ```bash
>   brew install git-lfs
>   git lfs install
>   ```
>
> * **Windows**:
>   Download and install from [https://git-lfs.com](https://git-lfs.com)

---

## Output Repository

The output data for this case study can be found here:
[Link to Output Repository](https://github.com/cadet/RDM-Example-Rectangular-Pulse-Output)
