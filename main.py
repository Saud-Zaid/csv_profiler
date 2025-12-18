'''from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import write_json, write_markdown'''

from src.exercise.mini_exercise_12_15 import *
from src.exercise.mini_exercise_12_16 import *
from src.csv_profiler.string import *
from src.csv_profiler.models import *
from src.csv_profiler.profiling import *

import sys, os, shutil

def main() -> None:
    '''rows = read_csv_rows("data/sample.csv")
    report = basic_profile(rows)
    write_json(report, "outputs/report.json")
    write_markdown(report, "outputs/report.md")
    print("Wrote outputs/report.json and outputs/report.md")'''
    
    #print(md_header("My Enemey"))
    #print(md_bullets(['a', 'b']))
    numbers = [{"key": 6, "2key": 8}, {"key": 7, "2key": 9}]
    
    print(profile_rows(numbers))
    
    #numbers = [7, 5, 5, "ks"]
    
    #print(infer_type(numbers))
    
    #print(column_values(numbers, "key"))
    
    #print(numeric_stats(numbers))
    
    #print(sys.path)
    #print(os.getcwd())
    #print(shutil.which("git"))
    
    #print(slugify("My Report 01"))
    
    #Saud = Person("Saud", 00)
    
    #print(Saud.age)
    
    

if __name__ == "__main__":
    main()