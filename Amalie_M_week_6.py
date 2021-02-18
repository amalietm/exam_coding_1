# Download the lsystem.py file below and add comments to it in the relevant places, describing what the code does.


# Set initial state of l-system
initial = "AB"

# Rules for the l-system
rules = {
	"A": "AB",
	"B": "A"
}
# Adding parameters the function will act on
def l_system(initial, rules, generation):
        
# Copy initial state into current variable
	current = initial
	
# Loop through how many generations we want
	for _ in range(0, generation):
		result = ""
		
# Loop to say what the corresponding new state will be
		for state in current:
			result += rules.get(state, state)
# Assign result to current
		current = result

	return current
# Loop how many generations to be printed
for i in range(0, 10):
	print( "{}: {}".format(i, l_system(initial, rules, i)) )
