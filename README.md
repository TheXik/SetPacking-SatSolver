# SetPacking-SatSolver Documentation

## Set Packing Problem Description

Set packing is a classical NP-complete problem in computational compleSity theory and combinatorics, and was one of Karp's 21 NP-complete problems. Suppose one has a finite set `S` and a subsets `S`. Then, the set packing problem asks if some `T` subsets are pairwise disjoint (in other words, no two of them share an element).

More formally, given a universe `U` and a family `S` of subsets of `U`, a packing is a subfamily `C ⊆ S` of sets such that all sets in `C` are pairwise disjoint. The size of the packing is `|C|`. 

The input is an integer : set_packing_size `T` and sets `S` each on different line splitted with a space.  
The question is whether there is a set packing of size `T` or more.


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

    first line`set packing size`

    second line `element_of_set element_of_set element_of_set .....`

    third line `element_of_set element_of_set element_of_set .....`

    fourth line `element_of_set element_of_set element_of_set .....`

    fifth line `...................`

    `.........................................`

    n-th line `....................`

    1. The first line specifies the target packing size, `T = 3`.
    2. Subsequent lines represent the subsets:
        - Set 1: 1 2
        - Set 2: 3 4
        - Set 3: 2 3
        - Set 4: 5
        - Set 5: 5 6

    The goal is to find at least 3 subsets that are pairwise disjoint (no overlapping elements)
    #### Output

    The SAT solver outputs the solution as SATISFIABLE. 
    And as we can see the 1. set  2. and 5. are pairwise disjoint they share no same element.


## Constraints
- For this problem I have chosen to use sets variables.

For each set in input I create a `Si` varibale that represents that the current `Si` set is selected `-Si`(negation) represents that set isnt in selected for the pairwise disjoint 

1. constraint is Disjointness of the sets 
We need to ensure that no two selected sets share the same element.
Traverse throught every pair of sets and check whether they have same element if yes then we add 
this clause to our cnf formula `(-Si v -Sj)`

This means that at least one of the two sets Si v Sj cannot be selected

2. Constraint is that we need to select at least T sets

We achive this with generating all possible combinations of length =`len(sets)`−(setpacking_size`T`)+1
Each subset represents a combination of sets that could be unselected

- Generating all possible combinations of length (l) - > (Si1,Si2,...,Sil)

- For each combination of variables(Si1,Si2,...,Sil) add clause to the cnf formula 
`(Si1 v Si2 v ...v Sil)`

This clause ensures that at least one of the sets in this combination is selected



## Basic Usage

Run the solver using the following command:

python3 set_packing.py [-h HELP] [-i INPUT] [-o OUTPUT] [-s SOLVER] [-v {0,1}]

### Command-line Options:

- `-h, --help`  
  Show a help message and exit.

- `-i INPUT, --input INPUT`  
  The instance file containing the input data. Default: `"instances/small_input_sat.in"`.

- `-o OUTPUT, --output OUTPUT`  
  Specify the output file for the DIMACS format CNF formula.

- `-s SOLVER, --solver SOLVER`  
  Specify the SAT solver to be used. Default: `glucose`.

- `-v {0,1}, --verb {0,1}`  
  Set the verbosity level of the SAT solver. `0` for minimal output and `1` for detailed output.


## Example Instances

Below is a table listing the example instances
## Example Instances

Below is a table listing the example instances, including their names, the number of sets, the target packing size (T), and the time taken to run:

| Instance Name                   | Number of Sets | Target Packing Size (T) | Time Taken (seconds) |
|---------------------------------|----------------|--------------------------|-----------------------|
| small_input_unsat | 5              | 3                        | 0.05                 |
| small_input_sat  | 10             | 5                        | 0.12                 |
| normal_running_time_input_unsat | 20             | 10                       | 0.45                 |
| normal_running_time_input_sat   | 6              | 2                        | 0.03                 |
| high_running_time_unsat         | 15             | 7                        | 0.25                 |
| high_running_time_sat           | 30             | 15                       | 1.10                 |
