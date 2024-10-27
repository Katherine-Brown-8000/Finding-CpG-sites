# Edit Where it says 'your_username' to match what your computers name is
# Edit where it says epigenetics_file_1 to whatever the name of your file it

file_name = r"C:\Users\your_username\Downloads\epigenetics_file_1.fa"

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
