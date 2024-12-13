# Getting inputs:
adjective = input(" Enter an adjective: ")
large_objects_plural = input(" Enter large_objects_plural: ")
body_part = input(" Enter a body_part: ")
restaurant = input(" Enter a restaurant: ")
first_food = input(" Enter a food: ")
second_food = input(" Enter another food: ")
large_object_singular = input(" Enter a large_object_singular: ")

# Inputs:
# adjective = "blue"
# large_objects_plural = "tables"
# body_part = "arm"
# restaurant = "Pizza Hut"
# first_food = "sushi"
# second_food = "pasta"
# large_object_singular = "airplane"


# Creating the story:
story = f"""
I’ve had a very {adjective} day.
This morning, I dropped a box of {large_objects_plural} on my {body_part}.
Then, at lunch, I went to {restaurant} for their delicious {first_food},
But the waiter brought me {second_food}, which I was not hungry for.
Finally, on my way home, I was cut off by a van with a large {large_object_singular} strapped to the roof.
"""

# New story
print(story)


# New story on Terminal: 
# I’ve had a very blue day.
# This morning, I dropped a box of tables on my arm.
# Then, at lunch, I went to Pizza Hut for their delicious sushi,
# But the waiter brought me pasta, which I was not hungry for.
# Finally, on my way home, I was cut off by a van with a large airplane strapped to the roof.
