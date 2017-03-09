# Advanced Programming Assessment is Below
# --------------------------------------------------------------------
# SeqIO was imported in order to begin file conversion.
from Bio import SeqIO
# Groupby was imported from itertools for class FastaFile.
from itertools import groupby

# A class created to parse FASTA file in a dictionary format.
# class used to ask user to input value
class FastaFile(object):
    # The '__init__' magic method was used to initialise the class
    def __init__(self, path):
        self.path = path
        # Map was used to help return a list of results.
        self._map = {}
        self.fastaiter()

    # 'fastaiter' was called as a function.
    # 'fastaiter' was used to help separate headings of the file.
    def fastaiter(self):
        fasta = open(self.path)
        # The variable 'fasta_iter' created the keys starting at '>'.
        fasta_iter = (x[1] for x in groupby
        (fasta,lambda line:line[0] == ">"))
        # A for loop separated headers of all records in the file.
        for header in fasta_iter:
            # Only 1:9 was used to get ID number without '>' or '.1'.
            header = header.next()[1:9].strip()
            # The sequence was added after the ID.
            seq = "".join(s.strip() for s in fasta_iter.next())
            self._map[header] = seq

    # '__getitem__' was used to define the behaviour of 'key'.
    # 'key' is referring to dictionary key.
    def __getitem__(self, key):
        return self._map[key]

    # '__iter__' was used to make function iterable.
    # It was able to return itself.
    def __iter__(self):
        # A for loop was made in function so it would be returned.
        # A dictionary was created.
        # Its output would be sequence ID and sequence line by line.
        for key in self._map:
            yield key, self._map[key]

    #Function created to look up input (ID) in the dictionary.
    #It then prints the sequence for associated ID.
    def user_input(self):

        #Loop was made and looped until told to stop.
        while True:
            # Command variable asked user for an input.
            # Command variable was the raw input user had typed.
            command = raw_input("Please provide sequence"
                " identification number (e.g. XXXXXXXX) "
                                "or type 'exit' to close: ")

            # If user typed exit 'command' stopped asking for input.
            if command.lower() == "exit":
                # A print statement appeared confirming 'exit'.
                 print "Farewell dear user. " \
                       "I hope that we will meet again someday soon."
                 break

            # If input did not match keys it asked for input again.
            if command not in self._map.keys():
                # An error message was printed if key was not valid.
                # Command variable was used to ask for input again.
                print "ERROR: '%s' is not a sequence" \
                       " identification number in the dictionary. " \
                       "Try again." % \
                command

            # If input was valid it searched for keys in dictionary.
            else:

                value = self.__getitem__(command)
                # Sequence ID and then sequence were printed.
                print "%s: %s" % (command, value)


# GenBank file was downloaded and set as variable 'genbank_file'.
genbank_file = ("/home/mika/AdvancedProgramming/GenBank")
# An empty FASTA file was created and set as  variable 'fasta_file'.
fasta_file = ("/home/mika/AdvancedProgramming/Obs.fasta")

# 'input' was created for when the GenBank file opened and read.
input = open(genbank_file, "r")
# 'output' was created for when the FASTA file opened and written in.
output = open(fasta_file, "w")

# A for loop was created to convert the sequence records.
# Records were converted from GenBank to empty FASTA file.
for sequence_record in SeqIO.parse(input, "genbank"):
    # Print statement was used to inform users of conversion.
    # ID number showed to tell which records were being converted.
    print "Converting GenBank record '%s'" % sequence_record.id
    # The ID, description and sequence of the records were converted.
    output.write(">%s %s\n%s\n" % (
        sequence_record.id,
        sequence_record.description,
        sequence_record.seq.tostring()))

# The GenBank file and the FASTA were closed.
output.close()
input.close()

# A print statement was used to say when the conversion was finished.
print "Conversion process completed."

 # class FastaFile was saved as 'cff' having FASTA file as object.
cff = FastaFile("/home/mika/AdvancedProgramming/Obs.fasta")

# A loop was created to print the dictionary from 'cff'.
for sequence_id, sequence in cff:
    print sequence_id, sequence

# Function within class was called using print statement.
print cff.user_input()
