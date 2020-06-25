'''
Got 24/24 on the checking
'''
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    if is_valid_sequence (dna):
        return len(dna)
    else:
        return 0

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if is_valid_sequence (dna1) and is_valid_sequence (dna2) and (len(dna1)>len(dna2)):
        return True
    else:
        return False



def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for data in dna:
        if data==nucleotide:
            count = count + 1
    
    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if is_valid_sequence (dna1) and is_valid_sequence (dna2) and (dna2 in dna1):
        return True
    else:
        return False

def is_valid_sequence (dna1):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid 
    (it contains no characters other than \verb|'A'|’A’, \verb|'T'|’T’, \verb|'C'|’C’ and \verb|'G'|’G’)

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCggC'
    False
    """
    isvalid = True
    for data in dna1:
        if not data in 'ATCG':
            isvalid = False
    return isvalid


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG’,’AT’,2)
    CCATGG
    """
    if (not is_valid_sequence (dna1)) or (not is_valid_sequence (dna2)):
        return''
    elif index>=len(dna1):
        return dna1+dna2
    else:
        return dna1[:index]+dna2+dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str

    Return the complement of the given nucleotide. 

    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    >>> get_complement('C')
    G
    >>> get_complement('T')
    A
    """
    if nucleotide =='A':
        return 'T'
    elif nucleotide =='G':
        return 'C'
    elif nucleotide =='C':
        return 'G'
    elif nucleotide =='T':
        return 'A'
    else:
        return ''
def get_complementary_sequence(dna1):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence. 

    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('ACGTACG')
    TGCATGC
    """ 
    complementary = ''   
    if is_valid_sequence(dna1):
        for data in dna1:
            complementary = complementary+get_complement(data)
    return complementary