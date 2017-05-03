# TestHeatIndexCalculator.py

# What are we testing for?

# Wide range of inputs
# Correct outputs


# Import Statements
import unittest
import HeatIndexCalculator

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription

    def test_calculateHeatIndex_forLowRelativeHumidity_WarmTemp(self):
        # Capture the results of the function
        result = HeatIndexCalculator.calculateHeatIndex(40, 80)
        # Check for expected output
        expected = 79
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forLowRelativeHumidity_HotTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(40, 92)
        expected = 93
        self.assertEqual(expected, result)

    # Add minimum of 5 more unittests
    def test_calculateHeatIndex_forLowRelativeHumidity_ExtremeHotTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(45, 108)
        expected = 136
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forMedRelativeHumidity_WarmTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(65, 80)
        expected = 82
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forMedRelativeHumidity_HotTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(65, 90)
        expected = 102
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forMedRelativeHumidity_ExtremeTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(60, 100)
        expected = 129
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forHighRelativeHumidity_WarmTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(95, 80)
        expected = 86
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forHighRelativeHumidity_HotTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(100, 90)
        expected = 131
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_for_80RelativeHumidity_94Temp(self):
        result = HeatIndexCalculator.calculateHeatIndex(80, 94)
        expected = 129
        self.assertEqual(expected, result)
        
    def test_calculateHeatIndex_for_70RelativeHumidity_98Temp(self):
        result = HeatIndexCalculator.calculateHeatIndex(70, 98)
        expected = 134
        self.assertEqual(expected, result)


# Run the tests
if __name__ == '__main__':
    unittest.main()
