import json
import random
from typing import List, Dict

class WorkoutGenerator:
    def __init__(self, exercises_file: str = "data/exercises.json"):
        with open(exercises_file, 'r') as f:
            data = json.load(f)
            self.exercises = data['exercises']
    
    def filter_exercises(self, level: str, equipment: str) -> Dict[str, List[Dict]]:
        """Filter exercises by level and equipment, grouped by category"""
        filtered = {
            'push': [],
            'pull': [],
            'legs': [],
            'core': []
        }
        
        for exercise in self.exercises:
            if level in exercise['level'] and equipment in exercise['equipment']:
                filtered[exercise['category']].append(exercise)
        
        return filtered
    
    def generate_workout(self, days_per_week: int, level: str, equipment: str) -> Dict:
        """Generate a workout plan based on user inputs"""
        filtered_exercises = self.filter_exercises(level, equipment)
        
        workout_plan = {
            'days_per_week': days_per_week,
            'level': level,
            'equipment': equipment,
            'workouts': []
        }
        
        if days_per_week == 3:
            workout_plan['workouts'] = self._generate_3_day_split(filtered_exercises)
        elif days_per_week == 4:
            workout_plan['workouts'] = self._generate_4_day_split(filtered_exercises)
        elif days_per_week == 5:
            workout_plan['workouts'] = self._generate_5_day_split(filtered_exercises)
        
        return workout_plan
    
    def _generate_3_day_split(self, exercises: Dict[str, List[Dict]]) -> List[Dict]:
        """Full body workouts - 3 days per week"""
        workouts = []
        
        for day in range(1, 4):
            workout = {
                'day': day,
                'name': f'Full Body Day {day}',
                'exercises': []
            }
            
            # Pick 1-2 from each category
            if exercises['push']:
                workout['exercises'].extend(random.sample(exercises['push'], min(2, len(exercises['push']))))
            if exercises['pull']:
                workout['exercises'].extend(random.sample(exercises['pull'], min(2, len(exercises['pull']))))
            if exercises['legs']:
                workout['exercises'].extend(random.sample(exercises['legs'], min(2, len(exercises['legs']))))
            if exercises['core']:
                workout['exercises'].extend(random.sample(exercises['core'], min(1, len(exercises['core']))))
            
            workouts.append(workout)
        
        return workouts
    
    def _generate_4_day_split(self, exercises: Dict[str, List[Dict]]) -> List[Dict]:
        """Upper/Lower split - 4 days per week"""
        workouts = []
        
        # Day 1: Upper (Push focus)
        workouts.append({
            'day': 1,
            'name': 'Upper Body - Push Focus',
            'exercises': (
                random.sample(exercises['push'], min(3, len(exercises['push']))) +
                random.sample(exercises['pull'], min(1, len(exercises['pull']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        # Day 2: Lower
        workouts.append({
            'day': 2,
            'name': 'Lower Body',
            'exercises': (
                random.sample(exercises['legs'], min(3, len(exercises['legs']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        # Day 3: Upper (Pull focus)
        workouts.append({
            'day': 3,
            'name': 'Upper Body - Pull Focus',
            'exercises': (
                random.sample(exercises['pull'], min(3, len(exercises['pull']))) +
                random.sample(exercises['push'], min(1, len(exercises['push']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        # Day 4: Lower
        workouts.append({
            'day': 4,
            'name': 'Lower Body',
            'exercises': (
                random.sample(exercises['legs'], min(3, len(exercises['legs']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        return workouts
    
    def _generate_5_day_split(self, exercises: Dict[str, List[Dict]]) -> List[Dict]:
        """Push/Pull/Legs split - 5 days per week"""
        workouts = []
        
        # Day 1: Push
        workouts.append({
            'day': 1,
            'name': 'Push Day',
            'exercises': (
                random.sample(exercises['push'], min(4, len(exercises['push']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        # Day 2: Pull
        workouts.append({
            'day': 2,
            'name': 'Pull Day',
            'exercises': (
                random.sample(exercises['pull'], min(4, len(exercises['pull']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        # Day 3: Legs
        workouts.append({
            'day': 3,
            'name': 'Leg Day',
            'exercises': (
                random.sample(exercises['legs'], min(4, len(exercises['legs']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        # Day 4: Push
        workouts.append({
            'day': 4,
            'name': 'Push Day',
            'exercises': (
                random.sample(exercises['push'], min(4, len(exercises['push']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        # Day 5: Pull
        workouts.append({
            'day': 5,
            'name': 'Pull Day',
            'exercises': (
                random.sample(exercises['pull'], min(4, len(exercises['pull']))) +
                random.sample(exercises['core'], min(1, len(exercises['core'])))
            )
        })
        
        return workouts


def generate_workout_json(days_per_week: int, level: str, equipment: str) -> str:
    """Main function to generate workout and return as JSON string"""
    generator = WorkoutGenerator()
    workout = generator.generate_workout(days_per_week, level, equipment)
    return json.dumps(workout, indent=2)


if __name__ == "__main__":
    # Test the generator
    print("=== Testing Workout Generator ===\n")
    
    # Test case 1: Beginner, 3 days, bodyweight only
    print("Test 1: Beginner, 3 days/week, bodyweight only")
    result = generate_workout_json(3, "beginner", "bodyweight")
    print(result)
    print("\n" + "="*50 + "\n")
    
    # Test case 2: Intermediate, 4 days, with pull-up bar
    print("Test 2: Intermediate, 4 days/week, pull-up bar")
    result = generate_workout_json(4, "intermediate", "pullup_bar")
    print(result)
