from Bio import SeqIO

genbank_file = ("/home/mika/AdvancedProgramming/GenBank")
fasta_file = ("/home/mika/AdvancedProgramming/obs.fasta")

input = open(genbank_file, "r")
output = open(fasta_file, "w")

for sequence_record in SeqIO.parse(input, "genbank"):
    print "Converting GenBank record '%s'" %sequence_record.id
    output.write(">%s %s\n%s\n" % (
        sequence_record.id,
        sequence_record.description,
        str(sequence_record)))

output.close()
input.close()


