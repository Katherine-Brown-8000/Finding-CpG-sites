# Edit Where it says 'your_username' to match what your computers name is
# Edit where it says epigenetics_file_1 to whatever the name of your file it

file_path = r'C:/Users/username/Desktop/epigenetics_file_1.txt'

def find_cpg_sites(sequence):

    cpg_sites = []
    for i in range(len(sequence) - 1):
        if sequence[i:i+2] == 'CG':
            cpg_sites.append(i)
    return cpg_sites

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
    return content

sequence = read_file(file_path)

cpg_sites = find_cpg_sites(sequence)
print("CpG sites found at indices:", cpg_sites)
