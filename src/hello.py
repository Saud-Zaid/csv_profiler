rows = [
	{"age":"19", "city": "Riyadh"},
	{"age":"", "city": "Jeddah"},
	{"age":"20", "city": ""}
]

row_count = len(rows)
missing_ages = 0
missing_cities = 0

for row in rows:
	for key in row:
		if key == "age" and  row[key] == "":
			missing_ages += 1
		if key == "city" and row[key] == "":
			missing_cities += 1

report = {
	"rows": row_count,
	"columns": {
		"age":{
			"missing": missing_ages,
			"type": "number"
		},
		"city": {
			"missing": missing_cities,
			"type": "string"
		}
	}
}

print(report)