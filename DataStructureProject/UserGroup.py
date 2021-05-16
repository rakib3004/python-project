def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for key,val in group_dictionary.items():
         for v in val:
            user_groups[v]=[]

         for v in val:
             user_groups[v].append(key)

			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))