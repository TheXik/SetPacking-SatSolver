# SetPacking-SatSolver Documentation

## Set Packing Problem Description

Set packing is a classical NP-complete problem in computational complexity theory and combinatorics, and was one of Karp's 21 NP-complete problems. Suppose one has a finite set `S` and a list of subsets of `S`. Then, the set packing problem asks if some `T` subsets are pairwise disjoint (in other words, no two of them share an element).

More formally, given a universe `U` and a family `S` of subsets of `U`, a packing is a subfamily `C ⊆ S` of sets such that all sets in `C` are pairwise disjoint. The size of the packing is `|C|`. 

The input is an integer : set_packing_size `T` and sets `S` each on different line split with space.  
The question is whether there is a set packing of size `T` or more.
I assume that number of sets is equal or greater than the set packing size


## How to Use

I am using sat solver `Glucose 4.2.1`.
###  Must install
1. `Python 3` 
2. A **UNIX-based system** (or WSL for Windows users).
3. A compiled version of the **Glucose SAT solver**:


## Input Format

- **Instance File**: The input file describes:
  - A target set packing size `T`.
  - A set of `n` subsets `S`, each defined on a separate line, with its elements
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

For each set in input I create a `Si` variable that represents that the current `Si` set is selected `-Si`(negation) represents that set isnt in selected

1. Constraint is disjointness of the sets 
We need to ensure that no two selected sets share the same element.
Traverse throught every pair of sets and check whether they have same element if yes then we add 
this clause to our cnf formula `(-Si v -Sj)`

This means that at least one of the two sets Si v Sj cannot be selected

2. Constraint is that we need to select at least T sets

We achieve this with generating all possible combinations of 
length =`len(sets)`−`(setpacking_size|T)`+1

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

Below is a table listing the example instances.

| Instance Name                   | Number of Sets | Set Packing Size (T) | Time Taken (seconds) |
|---------------------------------|----------------|--------------------------|-----------------------|
| small_input_unsat               | 5              | 3                        | 0.1                   |
| small_input_sat                 | 5              | 3                        | 0.1                   |
| normal_running_time_input_unsat | 24             | 6                        | 7.18                  |
| normal_running_time_input_sat   | 24             | 6                        | 7.01                  |
| medium_running_time_unsat       | 23             | 7                        | 32.58                 |
| medium_running_time_sat         | 23             | 7                        | 42.07                 |
| high_running_time_unsat         | 23             | 8                        | 94.78                 |
| high_running_time_sat           | 23             | 8                        | 98.78                 |


## Experiments
I have experimeted with this quite a bit when I was creating instances for this project, but some observations can be made.
The encoding can take big amount of time for larger instances for example when the number of sets
`30_sets_T4 - 111.92 sec encoding | satsolver close to 0 sec`
`20_sets_T12 - close to 0 sec encoding | satsolver 42.30 sec`
The sat solver will take bigger amount of time when there is larger `set_packing_size`