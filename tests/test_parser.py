from rxmarbles.generator import * 
import unittest

class NegativeParserTests(unittest.TestCase):
    
    def test_when_empty_diagram_given___exception_is_thrown(self):
        input = """
        marble foo { }
        """
        with self.assertRaises(ParseException):
            result = marble_diagrams.parseString(input)

    def test_empty_string_given___exception_is_thrown(self):
        input = ""
        with self.assertRaises(ParseException):
            result = marble_diagrams.parseString(input)
        
    def test_source_without_timeline_given___exception_is_thrown(self):
        input = """
        marble foo {
            source a:
         }
        """
        with self.assertRaises(ParseException):
            result = marble_diagrams.parseString(input)

    def test_diagram_without_end_brace_given___exception_is_thrown(self):
        input = """
        marble foo {
            source a: +-|
        """
        with self.assertRaises(ParseException):
            result = marble_diagrams.parseString(input)

    def test_source_without_unterminated_timeline_given___exception_is_thrown(self):
        input = """
        marble foo {
            source a: +--123--
         }
        """
        with self.assertRaises(ParseException):
            result = marble_diagrams.parseString(input)

class PositiveParserTests(unittest.TestCase):
    def test_when_simple_source_given___no_exception_is_thrown(self):
        input = "marble foo { source bar: +-| }"
        marble_diagrams.parseString(input)

class SingleMarbleSingleSourceWithOneNopCase(unittest.TestCase):
    def setUp(self):
        self.result = marble_diagrams.parseString("marble foo { source bar: +-| }")

    def test_result_list_has_single_marble_in(self):
        self.assertTrue(1, len(self.result[0]))
        
    def test_first_marble_has_one_timeline_in(self):
        self.assertTrue(1, self.result[0][0])

    def test_first_marble_has_foo_name_given(self):
        self.assertEqual("foo", self.result[0].diagram_name)
        
    def test_first_marbles_timeline_is_classified_as_source(self):
        timeline = self.result[0][1]
        self.assertEqual("source", timeline.type)

    def test_first_marbles_timeline_is_named_bar(self):
        timeline = self.result[0][1]
        self.assertEqual("bar", timeline.name)

    def test_first_marbles_timeline_has_only_one_nop_element(self):
        diagram = self.result[0]
        timeline = diagram[1]
        ticks = timeline[2].ticks
        self.assertEqual(1, len(ticks))
        self.assertEqual('-', ticks[0])
        
class SingleMarbleWithOneSourceAndOneOperatorWithOneNopCase(unittest.TestCase):
    def setUp(self):
        self.result = marble_diagrams.parseString("marble foo { source bar: +-| operator dog: +-| }")
        
    def test_result_list_has_single_marble_in(self):
        self.assertTrue(1, len(self.result))
        
    def test_marble_diagram_list_has_two_items_in(self):
        self.assertTrue(2, len(self.result[0]))

    def test_first_marble_has_one_timeline_in(self):
        self.assertTrue(1, self.result[0][0])

    def test_second_marble_has_one_timeline_in(self):
        self.assertTrue(1, self.result[0][1])


class MutlipleMarblesWithAllFeatures(unittest.TestCase):
    def setUp(self):
        self.input = """
            // some comment in the file
            marble A 
            {
                // some comment in the diagram
                source   A1: +--1-2-(12)-->
                operator A2: +--1-2-(12)-->    // some comment at the end of timeline
            }
            marble B
            {
                source B1: ...+--A-B-C--|
                source B2: ...+>
                source B3: ...+|
                source B4: ...+#
                source B5: ...+--#
            }
            marble C
            {
                source C1: +---1    --|
                source C2: +---{ABC}--|
                operator C3: 
                {
                    +--1-2-34     -4-|
                    ..+--1-2- 34  -4-|
                    .....+--A-(B1)-{CBA}-#
                }
            }
        """
    def test_when_parsed____no_exception_thrown(self):
        marble_diagrams.parseString(self.input)
        
class MarblesWithSpecialCharactersCase(unittest.TestCase):

    def test_when_diagram_has_special_characters_in_source_label____same_label_is_provided_in_object_model(self):
        input = """marble A 
            {
                source  abcABC123_<>?,./;'"[]\{}|`'~!@#$%^&*()_+-=: +-|
            }
        """
        result = marble_diagrams.parseString(input)
        self.assertEqual("""abcABC123_<>?,./;'"[]\{}|`'~!@#$%^&*()_+-=""", result[0][1].name)

    def test_when_diagram_has_special_characters_in_operator_label____same_label_is_provided_in_object_model(self):
        input = """marble A 
            {
                operator abcABC123_<>?,./;'"[]\{}|`'~!@#$%^&*()_+-=: +-|
            }
        """
        result = marble_diagrams.parseString(input)
        self.assertEqual("""abcABC123_<>?,./;'"[]\{}|`'~!@#$%^&*()_+-=""", result[0][1].name)

    def test_when_diagram_has_special_characters_in_marble_text____same_label_is_provided_in_object_model(self):
        input = """marble A
            {    
                source   A1: +--(abcABC123_-'".)-|
            }
        """
        result = marble_diagrams.parseString(input)
        diagram = result[0]
        timeline = diagram[1]
        events = timeline[2][0]
        print(timeline)
        self.assertEqual("""abcABC123_-'".""", events[2])
