# unittest and os was imported for Testing.
import unittest
import os

# class was created for testing if file exists
class TestFastaFile(TestCase):
    def test_file(self):
        file = "/home/mika/AdvancedProgramming/Obs.fasta"
        self.assertTrue(os.path.isfile(file))
    if __name__ == '__main__':
        unittest.main()