# Unittest and OS libraries were imported.
import unittest
import os

# class was created for testing if file exists
class TestFastaFile(unittest.TestCase):
    def test_file(self):
        file = "/home/mika/AdvancedProgramming/Obs.fasta"
        self.assertTrue(os.path.isfile(file))
    if __name__ == '__main__':
        unittest.main()