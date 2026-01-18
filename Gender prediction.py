from re import X
from os import name
import pandas as pd
import gender_guesser.detector as gender
df=pd.read_excel("gender_guess.xlsx")
name_col="Name" # Changed from "name" to "Name"
df['first_name']=df[name_col].str.strip().str.split().str[0].str.lower() # Corrected column name to 'first_name' and called .str.lower()
d=gender.Detector()
df['gender']=df['first_name'].apply(lambda x: d.get_gender(x)) # Corrected apply method
def clean_gender(g):
    if g in ['male', 'mostly_male']:
        return 'Male'
    elif g in ['female', 'mostly_female']:
        return 'Female'
    else:
        return 'Unknown'
male_names = ['sagar', 'revanth', 'venu', 'shankar']
female_names = ['megha']

def indian_gender(name, current_gender):
    if name in male_names:
        return 'Male'
    elif name in female_names:
        return 'Female'
    else:
        return current_gender

df['gender_final'] = df['gender'].apply(clean_gender) # Initialize 'gender_final' column
df['gender_final'] = df.apply(
    lambda row: indian_gender(row['first_name'], row['gender_final']),
    axis=1
)
output_file = "gender_fixed_output.xlsx"
df.to_excel(output_file, index=False)

print("Gender prediction completed")
print(" File saved as:", output_file)
files.download(output_file)
