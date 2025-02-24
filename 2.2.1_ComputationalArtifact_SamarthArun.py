categories = ["Salary", "Satisfaction", "Job Description", "Colleges", "Ethical Responsibilities"]

salary = "Entry-level (0-2 yrs): $40k-$60k, Mid-level (3-7 yrs): $65k-$90k, Senior (8-15 yrs): $95k-$130k, Lead (15+ yrs): up to $200k."
satisfaction = "The majority of game designers have a passion for their job so they get a lot of personal satisfaction."
job_description = "A game designer does the following things:\nDevelop core concept and theme of game\nCreate characters, settings, and narrative arcs that align with the game's tone and objectives.\nDesign the rules, challenges, and interactions that make up the gameplay.\nBalance difficulty, pacing, and progression to ensure the game is fun and engaging.\nBuild and test prototypes to refine mechanics and concepts.\nGather player feedback and iterate on the design to improve the experience.\nDesign levels or environments that align with the gameplay mechanics.\nEnsure levels are visually appealing and encourage exploration or strategic play.\nWork closely with programmers, artists, writers, and sound designers to bring the game to life.\nCommunicate the vision of the game to the entire team through design documents and pitches.\nCreate detailed game design documents outlining every aspect of the game for reference during development.\nStay informed about gaming trends and player preferences to design innovative games.\nFocus on how players interact with the game and ensure the interface is intuitive and enjoyable."
colleges = "Undergrad: New York University, University of Southern California, Clark University.\nGrad: University of Central Florida, New York University, University of Southern California."
ethical_responsibilities = "Game designers must avoid discrimination, stereotypes, and be responsible due to their global reach. They need to ensure that their games do not unintentionally promote harmful stereotypes or offensive content."

def info_display():
    print("What would you like to learn about game designers?")
    for category in categories:
        print(f"- {category}")
    print("- Exit")
    
    choice = input("I would like to learn about: ")
    
    if choice == "Salary":
        print(salary)
    elif choice == "Satisfaction":
        print(satisfaction)
    elif choice == "Job Description":
        print(job_description)
    elif choice == "Colleges":
        print(colleges)
    elif choice == "Ethical Responsibilities":
        print(ethical_responsibilities)
    elif choice.lower() == "exit":
        print("Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    
    return True

while True:
    if not info_display():
        break
    input("Press Enter to continue")
