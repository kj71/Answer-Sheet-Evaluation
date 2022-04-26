import os, io
import recognize_handwriting as rh
# import sentence_split as ss
import sementic_similarity as ss1

FOLDER_PATH = ''
IMAGE_FILE = r'Student_Answer.png'

FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

correct_answer = rh.recognize(FILE_PATH)
student_answer = rh.recognize('Student_Answer.png')
print(ss1.similarity_score(correct_answer, student_answer))

# correct_answer = ss.split_sentence(correct_answer)
# student_answer = ss.split_sentence(student_answer)
