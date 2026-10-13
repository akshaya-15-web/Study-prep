import random

def create_study_plan():
    print("\n===== StudyPrep: Exam Study Planner =====")

    subject = input("Enter your subject: ")
    days = int(input("How many days are left for your exam? "))

    topics_input = input("Enter topics separated by commas: ")
    topics = [topic.strip() for topic in topics_input.split(",") if topic.strip()]

    if days <= 0:
        print("Please enter a valid number of days.")
        return

    if not topics:
        print("Please enter at least one topic.")
        return

    print("\nCreating your study plan...")
    print("-" * 35)

    activities = [
        "Read notes and understand concepts",
        "Practice previous question papers",
        "Revise important questions",
        "Solve practice problems",
        "Review notes and take a mock test"
    ]

    for day in range(1, days + 1):
        topic_index = (day - 1) % len(topics)
        topic = topics[topic_index]

        print(f"\nDay {day}")
        print("Subject:", subject)
        print("Study Time: 3 hours")
        print("Topic:", topic)
        print("Activity:", activities[(day - 1) % len(activities)])

    print("\nStudy plan created successfully!")
    print("All the best for your exam!")


def study_tips():
    tips = [
        "Take short breaks between study sessions.",
        "Practice previous question papers.",
        "Revise important topics every day.",
        "Keep your phone away while studying."
    ]
    print("\nStudy Tip:", random.choice(tips))


while True:
    print("\n===== StudyPrep =====")
    print("1. Create Exam Study Plan")
    print("2. Get a Study Tip")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        create_study_plan()
    elif choice == "2":
        study_tips()
    elif choice == "3":
        print("Good luck with your exams! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")