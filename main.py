import random

def quiz_game():
    questions = [
        {
            "question": "Quelle est la capitale de la France ?",
            "reponse": "Paris"
        },
        {
            "question": "Combien font 2 + 2 ?", 
            "reponse": "4"
        },
        {
            "question": "De quelle couleur est le ciel ?",
            "reponse": "Bleu"
        }
    ]
    
    score = 0
    
    print("Bienvenue au Quiz!")
    print("Répondez aux questions suivantes:")
    print("---------------------------------")
    
    for q in questions:
        print("\n" + q["question"])
        reponse_utilisateur = input("Votre réponse: ")
        
        if reponse_utilisateur.lower() == q["reponse"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. La bonne réponse était: {q['reponse']}")
    
    print("\n---------------------------------")
    print(f"Quiz terminé! Votre score: {score}/{len(questions)}")
    
    if score == len(questions):
        print("Parfait! Vous avez tout bon!")
    elif score >= len(questions)/2:
        print("Bien joué!")
    else:
        print("Continuez à vous entraîner!")

if __name__ == "__main__":
    quiz_game()
