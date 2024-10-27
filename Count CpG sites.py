file_name = r"C:\Users\scien\Downloads\lambda_virus.fa"

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
        sequence = "".join([line.strip() for line in content if not line.startswith('>')])
    return sequence

sequence = read_file(file_name)

def find_cpg_sites(sequence):

    cpg_sites = []
    for i in range(len(sequence) - 1):
        if sequence[i:i+2] == 'CG':
            cpg_sites.append(i)
    return cpg_sites



cpg_sites = find_cpg_sites(sequence)
print("CpG sites found at indices:", cpg_sites)
num_cpg = len(cpg_sites)
print(f"The number of indices: {num_cpg}")
