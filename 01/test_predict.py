import unittest
from unittest import mock
from SomeModel import SomeModel, predict_message_mood


class TestPredict(unittest.TestCase):
    def setUp(self) -> None:
        self.model = SomeModel()

    def test_correct_predict_with_default_limits(self):
        with mock.patch("SomeModel.SomeModel.predict") as mock_model:
            mock_model.side_effect = [0.5, 0.0, 1.0]
            msg = "Test phrase"
            self.assertEqual("норм", predict_message_mood(msg, self.model))

            self.assertEqual("неуд", predict_message_mood(msg, self.model))

            self.assertEqual("отл", predict_message_mood(msg, self.model))

            expected_calls = [mock.call(msg)] * 3
            self.assertEqual(expected_calls, mock_model.mock_calls)


    def test_with_correct_user_limits(self):
        with mock.patch("SomeModel.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5
            msg = "Test phrase"
            self.assertEqual("неуд", predict_message_mood(msg, self.model, bad_thresholds=0.6))
            self.assertEqual("норм", predict_message_mood(msg, self.model, bad_thresholds=0.5))

            mock_model.return_value = 0.7
            self.assertEqual("отл", predict_message_mood(msg, self.model, good_thresholds=0.7))

    def test_with_incorrect_lower_limit(self):
        with mock.patch("SomeModel.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5
            msg = "Test phrase"
            with self.assertRaises(ValueError) as err:
                predict_message_mood(msg, self.model, bad_thresholds=-0.1)


    def test_with_incorrect_higher_limit(self):
        with mock.patch("SomeModel.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5
            msg = "Test phrase"
            with self.assertRaises(ValueError) as err:
                predict_message_mood(msg, self.model, good_thresholds=1.1)

    def test_when_lower_higher_than_high(self):
        with mock.patch("SomeModel.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5
            msg = "Test phrase"
            with self.assertRaises(ValueError) as err:
                predict_message_mood(msg, self.model, bad_thresholds=0.8, good_thresholds=0.5)

    def test_with_equal_limits(self):
        with mock.patch("SomeModel.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5
            msg = "Test phrase"
            with self.assertRaises(ValueError) as err:
                predict_message_mood(msg, self.model, bad_thresholds=0.5, good_thresholds=0.5)

    def test_with_incorrect_str_argument(self):
        with mock.patch("SomeModel.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5
            msg = "Test phrase"
            with self.assertRaises(ValueError) as err:
                predict_message_mood([1, 2], self.model)
                predict_message_mood(dict(), self.model)

    def test_wigh_incorrect_arguments_count(self):
        with mock.patch("SomeModel.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5
            msg = "Test phrase"
            with self.assertRaises(TypeError) as err:
                predict_message_mood(msg, msg, self.model, 0.2, 0.6)

if __name__ == '__main__':
    unittest.main()
