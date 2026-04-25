# 🤖 AI Calisthenics Workout Generator (POC)

A proof-of-concept workout generator that uses pre-computed exercise combinations to create personalized calisthenics programs. Users get the experience of AI-generated workouts with instant, deterministic results.

## 🎯 Concept

Instead of using real-time AI inference, this system:

- Stores exercises in a JSON database
- Uses rule-based Python algorithm to select appropriate exercises
- Presents results as "AI-generated" for better UX
- Allows easy expansion of exercise database over time

## 📁 Project Structure

```text
calisthenics-poc/
├── data/
│   └── exercises.json      # Exercise database
├── generator.py            # Selection algorithm
├── server.py              # Flask web server
├── index.html             # User interface
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Flask

### Installation

1. Install Flask:

```bash
pip install flask
```

2. Run the server:
```bash
python server.py
```

3. Open browser:

```text
http://localhost:5000
```

## 🎮 How to Use

1. **Select Training Days**: Choose 3, 4, or 5 days per week
2. **Select Fitness Level**: Beginner, Intermediate, or Advanced
3. **Select Equipment**: Bodyweight only, Pull-up bar, Rings, or Full setup
4. **Generate**: Click the button and get your workout plan!

## 🔧 Testing the Algorithm

Run the generator directly to test:

```bash
python generator.py
```

This will output sample workout plans for different configurations.

## 📊 Current Exercise Database

- **18 exercises** across 4 categories:
  - Push (4 exercises)
  - Pull (4 exercises)
  - Legs (5 exercises)
  - Core (5 exercises)

## 🎨 Workout Splits

### 3 Days/Week

- Full body workouts
- Balanced muscle group distribution

### 4 Days/Week

- Upper/Lower split
- Alternating push/pull focus

### 5 Days/Week

- Push/Pull/Legs split
- Dedicated muscle group days

## 🔮 Future Enhancements

- [ ] Add more exercises to database
- [ ] Include warm-up and cool-down routines
- [ ] Add progression tracking
- [ ] Export workout to PDF
- [ ] Use real AI to expand exercise variations
- [ ] Add video demonstrations

## 💡 Adding New Exercises

Edit `data/exercises.json` and add new exercise objects:

```json
{
  "id": "unique_id",
  "name": "Exercise Name",
  "category": "push|pull|legs|core",
  "level": ["beginner", "intermediate", "advanced"],
  "equipment": ["bodyweight", "pullup_bar", "rings", "full_setup"],
  "muscle_groups": ["muscle1", "muscle2"],
  "sets": 3,
  "reps": "8-12"
}
```

## 📝 Notes

- This is a POC - focus is on functionality, not perfection
- Exercise selection uses randomization for variety
- Equipment options are hierarchical (full_setup includes all equipment)
- Level filtering ensures appropriate difficulty
