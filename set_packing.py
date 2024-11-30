import subprocess
from argparse import ArgumentParser

def load_instance(input_file):
    print("- LOADING INPUT FILE")
    with open(input_file, "r") as f:
        lines = f.readlines()
       
    set_packing_size = int(lines[0].strip())
    sets = []
    
    for line in lines[1:]:
        num = list(map(int, line.strip().split()))
        sets.append(num)
    return sets, set_packing_size


def encode(sets, set_packing_size):
    print(" - ENCODING SET PACKING PROBLEM")
    cnf = []

    # CONSTRAINTS FOR SET PACKING

    for i, set1 in enumerate(sets,start= 1): 
        for j, set2 in enumerate(sets[i:], start=i + 1):
            for x in set1:
                for y in set2:
                    if x == y: # if the elements of the set are same then the sets are not disjoint therefore add set as variable to cnf 
                        cnf.append([-i, -j,0])

    length = len(sets) - set_packing_size + 1
    
    combinations_list = []
    create_comb(0, [], length, sets, combinations_list)
    for combination in combinations_list:
        cnf.append([i + 1 for i in combination] + [0])

    return cnf

def create_comb(start, curr_combination, combination_size, sets, combinations_list):
    if len(curr_combination) == combination_size:
        combinations_list.append(curr_combination.copy())
        return

    for i in range(start, len(sets)):
        curr_combination.append(i)
        create_comb(i + 1, curr_combination, combination_size, sets, combinations_list)
        curr_combination.pop()
        
    


def run_solver(cnf, nr_vars, output_name, solver_name, verbosity):
    print(" - CALLING SAT SOLVER")
    with open(output_name, "w") as f:
        f.write("p cnf {} {}\n".format(nr_vars, len(cnf)))
        for clause in cnf:
            f.write(" ".join(map(str, clause)) + "\n")
    return subprocess.run(['./' + solver_name, '-model', '-verb=' + str(verbosity) , output_name], stdout=subprocess.PIPE)
    
    
def print_output_result(result,sets):
    
    print(result.stdout.decode('utf-8'))
    if result.returncode == 20:
        return
    print("--------------PRINTING HUMAN READABLE OUTPUT RESULT--------------")
    print("\n")
    for line in result.stdout.decode('utf-8').split("\n"):
        if line.startswith("v"):
            values = line.split()[1:]
            for i,value in  enumerate(values):
                if value == "0":
                    break
                if int(value)<0:
                    continue
                print(i+1, end="")
                print(".set | ELEMENTS :", end=" ")
                for j,element in enumerate(sets[i]):
                    print(element, end=" ")
                print("\n")
            return
    

if __name__ == "__main__":
    
    # parse arguments
    parser = ArgumentParser()
    parser.add_argument("-i","--input",default="instances/small_input_sat.in",type=str,help=("The instance file."))
    parser.add_argument("-o", "--output", default="formula.cnf", type=str, help=("The output file of cnf formula."))
    parser.add_argument("-s", "--solver", default="glucose", type=str, help=("The solver to be used. Default is glucose."))
    parser.add_argument("-v", "--verbosity", default=1, type=int, help=("The verbosity level of the sat solver. Default is 1."))
    args = parser.parse_args()
    
    # load the instance from the input file
    sets,set_packing_size = load_instance(args.input)

    # encode(sets, set_packing_size)
    cnf =encode(sets,set_packing_size) # returns encoded formula
    
    # run sat solver on the cnf formula
    result = run_solver(cnf, len(sets), args.output, args.solver, args.verbosity)

    # print human readable output
    print_output_result(result,sets)
