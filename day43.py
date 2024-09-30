class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def main():
    questions = [
        Question("What is the capital of France?\n(a) Berlin\n(b) Paris\n(c) Madrid\n", "b"),
        Question("What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n", "b"),
        Question("What is the largest ocean?\n(a) Atlantic\n(b) Indian\n(c) Pacific\n", "c"),
    ]

    score = 0
    for q in questions:
        answer = input(q.prompt)
        if answer.lower() == q.answer:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    print(f"\nYou scored {score}/{len(questions)}.")

if __name__ == "__main__":
    main()
