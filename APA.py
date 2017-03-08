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
        sequence_record.seq.tostring()))

output.close()
input.close()

print "Conversion process completed."

from itertools import groupby

class FastaFile(object):
    def __init__(self, path):
        self.path = path
        self._map = {}
        self.__fasta_iter()

    def __str__(self):
        return self._map.__str__()

    def __fasta_iter(self):
        fasta = open(self.path)
        fasta_iter = (x[1] for x in groupby(fasta, lambda line: line[0] == ">"))
        for header in fasta_iter:
            header = header.next()[1:9].strip()
            seq = "".join(s.strip() for s in fasta_iter.next())
            self._map[header] = seq

    def getitem(self, k):
        return self._map[k]

    def __iter__(self):
        for k in self._map:
            yield k, self._map[k]

cff = FastaFile("/home/mika/AdvancedProgramming/obs.fasta")

for sequence_id, sequence in cff:
    print sequence_id, sequence


