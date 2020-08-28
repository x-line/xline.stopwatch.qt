import unittest
import xml.etree.ElementTree as ET
from models.Timers import Timers
from models.Timer import Timer
from models.TimerGroup import TimerGroup


TEST_FILE_NAME = 'tests/Timers unittest v.1.xml'

class LearningCase(unittest.TestCase):
    def test_dom(self):
        timers = Timers(TEST_FILE_NAME)
        timer = timers.get_or_create("Dirk's Timer")
        timer.start()
        lap = timer.stop("pretty test")

        # timers.save()
        xml = timers.as_xml_element
        Timers.write(xml, TEST_FILE_NAME)

        timers = Timers(TEST_FILE_NAME)
        timer = timers.get("Dirk's Timer")
        self.assertIsNotNone(timer)

        lap = timer.GetLastFluent()
        self.assertEqual(lap.task, "pretty test")


# def main():
#     unittest.main()

# if __name__ == "__main__":
#     main()

if __name__ == '__main__':
    unittest.main()


# python -m unittest tests.pretty_test -v