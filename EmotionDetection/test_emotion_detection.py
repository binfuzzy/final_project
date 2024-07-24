import unittest
from emotion_detection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    def test1(self):
        self.assertEqual(emotion_detection("I am glad this happened")['dominant_emotion'], 'joy')

    def test2(self):
        self.assertEqual(emotion_detection("I am really mad about this")['dominant_emotion'], 'anger')

    def test3(self):
        self.assertEqual(emotion_detection("I feel disgusted just hearing about this")['dominant_emotion'], 'disgust')

    def test4(self):
        self.assertEqual(emotion_detection("I am so sad about this")['dominant_emotion'], 'sadness')

    def test5(self):
        self.assertEqual(emotion_detection("I am really afraid that this will happen")['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()