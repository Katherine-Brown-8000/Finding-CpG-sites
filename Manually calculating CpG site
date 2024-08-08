sequence = "ATCGCGATCGCTAGCGCGGATCGCG"

def find_cpg_sites(sequence):

    cpg_sites = []
    for i in range(len(sequence) - 1):
        if sequence[i:i+2] == 'CG':
            cpg_sites.append(i)
    return cpg_sites

cpg_sites = find_cpg_sites(sequence)
print("CpG sites found at indices:", cpg_sites)
