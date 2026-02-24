from day5_utils import add, remove_spaces, average, introduce, clean_names

user = {
    "name": "Arslan",
    "age": 20,
    "skills": ["python", "logic", "dedication"],
}

raw = ["  Arslan  ", "ALI", "  hina", "ZARA  ", "daNish"]

introduce(user)

print(clean_names(raw))
