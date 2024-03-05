import random

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

questions = [
    Question("What is the capital of India?", ["Delhi", "Mumbai", "Kolkata", "Chennai"], "Delhi"),
    Question("Who is known as the 'Father of the Indian Constitution'?", [ "Jawaharlal Nehru", "B.R. Ambedkar","Mahatma Gandhi", "Sardar Vallabhbhai Patel"], "B.R. Ambedkar"),
    Question("What is the chemical symbol for gold?", ["Ag", "Au","Fe", "Cu"], "Au"),
    Question("Which of the following is the largest state by area in India?", ["Maharashtra", "Rajasthan", "Uttar Pradesh", "Madhya Pradesh"], "Rajasthan"),
    Question("Which Indian city is known as the 'Pink City'?", [ "Jodhpur", "Udaipur","Jaipur", "Ajmer"], "Jaipur"),
    Question("Who discovered the theory of relativity?", ["Isaac Newton","Albert Einstein", "Galileo Galilei", "Stephen Hawking"], "Albert Einstein"),
    Question("Which planet is known as the 'Red Planet'?", [ "Venus", "Jupiter", "Saturn","Mars"], "Mars"),
    Question("What is the tallest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "Mount Everest"),
    Question("Who is the current Prime Minister of India?", ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Manmohan Singh"], "Narendra Modi"),
    Question("What is the capital of Australia?", ["Canberra", "Sydney", "Melbourne", "Perth"], "Canberra"),
    Question("Which of the following is not a primary color?", ["Red", "Blue", "Yellow","Green"], "Green"),
    Question("Which river is known as the 'Ganga of the South'?", ["Godavari", "Krishna", "Cauvery", "Yamuna"], "Cauvery"),
    Question("Who is the CEO of Tesla Motors?", ["Elon Musk", "Jeff Bezos", "Mark Zuckerberg", "Tim Cook"], "Elon Musk"),
    Question("Which of the following is not a greenhouse gas?", [ "Carbon Dioxide","Oxygen", "Methane", "Nitrous Oxide"], "Oxygen"),
    Question("What is the currency of Japan?", ["Dollar", "Euro","Yen", "Pound"], "Yen"),
    Question("Who wrote 'The Great Gatsby'?", ["Ernest Hemingway", "William Faulkner", "Harper Lee","F. Scott Fitzgerald"], "F. Scott Fitzgerald"),
    Question("What is the largest organ in the human body?", [ "Liver","Skin", "Brain", "Heart"], "Skin"),
    Question("Which ocean is the largest?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "Pacific Ocean"),
    Question("Who is known as the 'Missile Man of India'?", ["Dr. A.P.J. Abdul Kalam", "Jawaharlal Nehru", "Indira Gandhi", "Sardar Vallabhbhai Patel"], "Dr. A.P.J. Abdul Kalam"),
    Question("What is the chemical symbol for water?", ["O2","H2O", "CO2", "H2SO4"], "H2O"),
    Question("Which planet is known as the 'Morning Star'?", ["Venus", "Mercury", "Mars", "Jupiter"], "Venus"),
    Question("Who is the author of 'Harry Potter' series?", ["Stephenie Meyer", "George R.R. Martin", "J.R.R. Tolkien","J.K. Rowling"], "J.K. Rowling"),
    Question("What is the currency of China?", ["Dollar", "Euro","Yuan", "Pound"], "Yuan"),
    Question("Which is the smallest state in India by area?", [ "Sikkim","Goa", "Manipur", "Tripura"], "Goa"),
    Question("Who painted the Mona Lisa?", ["Vincent van Gogh","Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], "Leonardo da Vinci"),
    Question("What is the study of earthquakes called?", ["Seismology", "Meteorology", "Geology", "Botany"], "Seismology"),
    Question("Which gas is responsible for the ozone layer depletion?", ["Chlorofluorocarbons", "Carbon Dioxide", "Oxygen", "Nitrogen"], "Chlorofluorocarbons"),
    Question("Which of the following is not a programming language?", ["HTML", "Python", "Java", "Adobe Photoshop"], "Adobe Photoshop"),
    Question("What is the national animal of India?", ["Lion", "Elephant","Tiger", "Leopard"], "Tiger"),
    Question("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"], "Alexander Graham Bell"),
    Question("What is the chemical symbol for iron?", ["Au","Fe","Ag", "Cu"], "Fe"),
    Question("Which city is known as the 'City of Lakes' in India?", ["Jaipur","Udaipur", "Bhopal", "Kochi"], "Udaipur"),
    Question("Who is the first woman Prime Minister of India?", ["Indira Gandhi", "Sonia Gandhi", "Pratibha Patil", "Margaret Thatcher"], "Indira Gandhi"),
    Question("Which is the hottest continent on Earth?", ["Asia", "Australia","Africa", "Europe"], "Africa"),
    Question("What is the chemical symbol for silver?", ["Ag", "Au", "Cu", "Fe"], "Ag"),
    Question("Who developed the theory of evolution?", ["Isaac Newton","Charles Darwin", "Albert Einstein", "Gregor Mendel"], "Charles Darwin"),
    Question("Which planet is known as the 'Blue Planet'?", ["Earth", "Mars", "Venus", "Jupiter"], "Earth"),
    Question("Who is the founder of Microsoft?", ["Steve Jobs","Bill Gates", "Larry Page", "Mark Zuckerberg"], "Bill Gates"),
    Question("Which country is known as the 'Land of the Rising Sun'?", ["China", "India", "South Korea","Japan"], "Japan"),
    Question("What is the chemical symbol for carbon?", [ "Ca","C","Co", "Cr"], "C"),
    Question("Which is the largest bone in the human body?", [ "Tibia","Femur", "Humerus", "Radius"], "Femur"),
    Question("Who was the first person to set foot on the moon?", ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"], "Neil Armstrong"),
    Question("Which country is known as the 'Land of the Midnight Sun'?", ["Norway", "Sweden", "Finland", "Iceland"], "Norway"),
    Question("What is the chemical symbol for potassium?", [ "P","K","Ka", "Po"], "K"),
    Question("Who discovered penicillin?", ["Louis Pasteur", "Jonas Salk","Alexander Fleming", "Edward Jenner"], "Alexander Fleming"),
    Question("Which city is known as the 'City of Dreams'?", ["Mumbai", "Delhi", "Kolkata", "Chennai"], "Mumbai"),
    Question("Who is known as the 'Nightangle of India'?", ["Sarojini Naidu", "Indira Gandhi", "Mother Teresa", "Lata Mangeshkar"], "Sarojini Naidu"),
    Question("What is the chemical symbol for sodium?", ["No", "Ne", "Ni","Na"], "Na"),
    Question("Who discovered gravity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"], "Isaac Newton"),
    Question("Which country is known as the 'Land of Thousand Lakes'?", ["Sweden", "Norway", "Denmark","Finland"], "Finland"),
    Question("What is the chemical symbol for helium?", ["He", "H", "Ha", "Ho"], "He"),
    Question("Who is the CEO of Apple Inc.?",["Steve Jobs", "Bill Gates", "Elon Musk","Tim Cook"], "Tim Cook"),
    Question("What is the chemical symbol for nitrogen?", ["Ni","N","Na", "Ne"], "N")
]

import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def run_quiz(self):
        self.shuffle_questions()  
        for question in self.questions:
            print(question.prompt)
            for i, option in enumerate(question.options, 1):
                print(f"{i}. {option}")

            user_input = input("Enter your choice (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                print("Quitting the quiz.")
                return self.score

            if user_input.isdigit():
                user_answer = int(user_input) - 1
                if 0 <= user_answer < len(question.options):
                    if question.options[user_answer] == question.answer:
                        self.score += 1
                        print("Correct!")
                    else:
                        print("Incorrect.")
                else:
                    print("Invalid option!")
            else:
                print("Please enter a number.")

        print(f"You got {self.score}/{len(self.questions)} correct.")
        return self.score

quiz = Quiz(questions)

score = quiz.run_quiz()
print("Your score is:", score)