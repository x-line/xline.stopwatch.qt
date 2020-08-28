import unittest
import xml.etree.ElementTree as ET
from models.Timers import Timers
from models.Timer import Timer
from models.TimerGroup import TimerGroup
from models.Fluent import Fluent


TEST_FILE_NAME = 'tests/Timers unittest v.1.xml'

class LearningCase(unittest.TestCase):
    def test_dom(self):
        tree = ET.parse(TEST_FILE_NAME)
        root = tree.getroot()
        print(root) # Timer

        last_timer = None
        for x in root.findall('./Timer'):
            last_timer = x



        for x in root.iter():
            print(x)

        # Add lap test:
        if False:
            lap = Fluent.CreateStart()
            lap.task = "whitespace test"
            lap.stop()
            xmllap = lap.as_xml_element
            # xmllap.text = "\t\t"
            # xmllap.tail = "\n"
            last_timer.append(xmllap)

        for lap in tree.findall('.//lap'):
        # for x in root.findall('.//lap'):
        # for x in root.iter('lap'):
            lap.tail = '\n    '

        for x in tree.iter('Timer'):
            x.text = '\n    '
            x.tail = '\n'

        root.text = '\n  '


        # timer = timers.get_or_create("Dirk's Timer")
        # timer.start()
        # lap = timer.stop("message")

        # # Save:
        tree.write(TEST_FILE_NAME)


        # Saving with pretty minidom adds whitespace each time if you write back out the same elements directly:
        # Timers.write(root, TEST_FILE_NAME)

        # timers = Timers(TEST_FILE_NAME)
        # timer = timers.get("Dirk's Timer")
        # self.assertIsNotNone(timer)

        # lap = timer.GetLastFluent()
        # self.assertEqual(lap.task, "message")


# def main():
#     unittest.main()

# if __name__ == "__main__":
#     main()

if __name__ == '__main__':
    unittest.main()


# python -m unittest tests.whitespace_test -v