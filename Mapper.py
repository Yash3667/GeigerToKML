def map_data(data):
	# Handle strange cases
	if len(data) == 1:
		entry = data[0]
		radlvl = calc_rads(entry)
		make_marker(get_point(entry), radlvl)

	while len(data) > 1:
		# Make a new path
		path = []

		# Calculate the radiation lvl of the path
		rad_one = calc_rads(data[0])
		rad_two = calc_rads(data[1])

		rad_lvl = (rad_one + rad_two) // 2

		# Extract the lat and long and put them on the path
		path.append(data[0])
		del data[0]
		path.append(data[0])

		rad_one = calc_rads(path[0])
		rad_two = calc_rads(path[0])

		rad_lvl = (rad_one + rad_two) // 2

		# Add additional points to the path, if applicable
		while len(data) > 1:
			path.append(data[0])

			if calc_rads(data[1]) == radlvl:
				del data[0]
			else:
				break

		make_path(path, radlvl)

def get_point(entry):
	return [entry[4], entry[5]]