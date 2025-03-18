#ask for user input
name = input('What is your name?')
color = input('What is your favorite color')
print(f'Hello, {name}! Your favorite color, {color}, is awesome!')


#game development QA
def run_quiz():
    questions = [
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A. func", "B. def", "C. define", "D. function"],
            "answer": "B"
        },
        {
            "question": "Which movie won the Oscar for Best Picture in 2023?",
            "options": ["A. Avatar: The Way of Water", "B. Everything Everywhere All at Once", "C. Top Gun: Maverick", "D. The Fabelmans"],
            "answer": "B"
        },
        {
            "question": "Which animal is known as the king of the jungle?",
            "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Cheetah"],
            "answer": "C"
        }
    ]
    
    score = 0
      

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")
    
    print(f"\n🏆 You scored {score} out of {len(questions)}!")

while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 🎉")
        break


# python jokes
import random

# List of programming jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why was the Python programmer so calm? Because he had 'try' and 'except' to handle problems! 😆",
    "How do you comfort a JavaScript bug? You console it. 😜",
    "Why did the programmer quit his job? Because he didn't get arrays (a raise)! 😂",
    "Why do Python developers wear glasses? Because they can't C! 🤓",
    "Why was the function feeling stressed? It had too many arguments! 😅",
    "Why do Java developers wear glasses? Because they don’t see sharp! 🤖",
    "What is a programmer's favorite place? The Foo Bar. 🍻",
]

# Randomly select and display a joke
print("\n🤣 Here's a joke for you:")
print(random.choice(jokes))
