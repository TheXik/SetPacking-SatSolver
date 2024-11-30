# SetPacking-SatSolver Documentation

## Set Packing Problem Description

Set packing is a classical NP-complete problem in computational complexity theory and combinatorics, and was one of Karp's 21 NP-complete problems. Suppose one has a finite set `S` and a subsets `S`. Then, the set packing problem asks if some `T` subsets are pairwise disjoint (in other words, no two of them share an element).

More formally, given a universe `U` and a family `S` of subsets of `U`, a packing is a subfamily `C ⊆ S` of sets such that all sets in `C` are pairwise disjoint. The size of the packing is `|C|`. 

The input is a `n` number of sets each on different line `S` and an integer : set_packing_size `T`
- The question is whether there is a set packing of size `T` or more.


## How to Use

I am using sat solver `Glucose 4.2.1`.

### To compile you need

1. `Python 3` installed
2. A **UNIX-based system** (or WSL for Windows users).
3. A compiled version of the **Glucose SAT solver**:


## Input Format

- **Instance File**: The input file describes:
  - A target set packing size `T`.
  - A set of `n` subsets `S`, each defined on a separate line.
- **Example Input** (`instances/small_input_sat.in`):
