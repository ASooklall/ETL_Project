# SQL Database Script for PokeDex and TrainerDex
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from config import password


# Set locations for CSV Files and create dataframes
csv_file1 = "pokedex_clean.csv"
pokedex_df = pd.read_csv(csv_file1)

csv_file2 = "trainer_clean.csv"
trainer_df = pd.read_csv(csv_file2)

csv_file3 = "trainer_junction_clean.csv"
trainer_junction_df = pd.read_csv(csv_file3)


# Connect to PostgreSQL
rds_connection_string = "postgres:"+password+"@localhost:5432/pokemon_db"
engine = create_engine(f'postgresql://{rds_connection_string}')

## Get Table Names
# engine.table_names()

# Read Dataframes into SQL and replace table if exists
pokedex_df.to_sql(name='pokedex', con=engine, if_exists='replace', index=False)
trainer_df.to_sql(name='trainer', con=engine, if_exists='replace', index=False)
trainer_junction_df.to_sql(name='trainer_junction', con=engine, if_exists='replace', index=False)


## Search Queries Test

# x = pd.read_sql_query('select * from pokedex LIMIT 20', con=engine)
# y = pd.read_sql_query('SELECT COUNT (*) FROM trainer', con=engine)
# z = pd.read_sql_query('select * from trainer_junction LIMIT 20', con=engine)
# print(x)
# print(y)
# print(z)



# Search Function
# Resume_Search is a nested inner function that allows the user to choose whether or not they want to search again.
def search():
    def resume_search():
        resume = input ("Would you like to search again? (Yes or No) ")
        if resume in ["yes","Yes","yEs","yeS","YEs","yES","YeS","YES","y","Y"]:
            search()
        else:
            print ('Search Canceled. Ending Prompt.')

    request = 0
    request = input ("What would you like to search for? (Select the number of the menu option)\
        \n1: Trainer Name Containing:\
        \n2: Trainers that own (name of pokemon):\
        \n3: Pokedex Entry for (pokemon name):\
        \n4: Pokedex Entry for (dex number):\
        \n0: Cancel search and end program.:\
        \nMenu Number: ")

    if request == 1 or request == str(1):
        print('1')
        resume_search()

    elif request == 2 or request == str(2):
        print ('2')
        resume_search()

    elif request == 3 or request == str(3):
        poke_name = input('What is the name of the pokemon whose pokedex entry you wish to search for? \nPokemon Name: ')
        search_return3 = pd.read_sql_query("SELECT * FROM pokedex WHERE pokemon_name = " + "'" + str((poke_name).title()) + "'", con=engine)
        print(search_return3)
        resume_search()

    elif request == 4 or request == str(4):
        poke_num = input('What is the pokedex number of the pokemon whose pokedex entry you wish to search for? \
            \nPlease note that we have our own pokedex numbering system. \
            \nPokedex Number: ')
        search_return4 = pd.read_sql_query("SELECT * FROM pokedex WHERE pokedex_number = " + "'" + str(poke_num) + "'", con=engine)
        print(search_return4)
        resume_search()

    elif request == 0 or request == str(0):
        print ('Search Canceled. Ending Prompt.')

    else:
        request = 0
        print ("That isn't a menu option number. Please try again.")
        search()

# Call the search function
search()