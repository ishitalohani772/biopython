# seqrecord
# how to create seqrecord
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
dna = Seq("ATGGCCTTTAAGGT")
record = SeqRecord(
    dna,
    id = "gene",
    name = "human gene",
    description= "sample dna"
)
print(record.id)
print(record.name)
print(record.description)
protein_seq = Seq("MKTIVV")
protein_record = SeqRecord(protein_seq,
                      "prot01",      #id
                          "test protein",     #name
                          "sample protein"    #decription
)
print(protein_record.id)
print(protein_record.name)
print(protein_record.description)
#create a dna sequence "ATGCGT" using biopython and print the sequence
dna_sequence = Seq("ATGCGT")
print(dna_sequence)
# given the DNA seq "ATGC", write code to print- complement, transcribed RNA
dna = Seq("ATGC")
print(dna)
print(dna.complement())
print(dna.transcribe())

# create a seq record with :
#id = "gene1"
# description = "sample gene sequence"
seq_folder = SeqRecord( dna,
                       id = "gene1",
                       description = "sample gene sequence"
)
print(seq_folder.id)

# create two sequence records :
#id = "geneA", seq = "ATGC"
#id = "geneB", seq = "TTAA"
# store them in a list and priny each id using a for loop
#working with FASTA files using biopython (SeqIO)
from Bio import SeqIO
record = SeqIO.read("cox.fasta","fasta")
print(record.id)
print(record.description)
print(len(record))
# insulin
record = SeqIO.read("MHCclass1.fasta","fasta")
print(record.id)
print(record.description)
print(len(record))
# introduction to GenBank files
record = SeqIO.read("COX1.gb","genbank")
print(record.id)
print(record.description)
print(record.annotations)
print(len(record.features))
# parse is use for studying multiple sequence at a time
for record in SeqIO.parse("cox.fasta","fasta"):
    print(record.id)
print(record.description)
print(len(record))
print("-"*30)
# to know the value of features
for feature in record.features:
    print(feature.type)
    # to know the location 
    print(feature.type,feature.location)






