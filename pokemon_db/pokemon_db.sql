-- SQL Database Script for PokeDex and TrainerDex
-- Follow instructions for setting up or updating database, default is creation of a new database


-- BEGIN DROP SECTION --
-- Drop Tables before creating new tables to prevent duplicates, comment out if you are not creating/recreating a new database
DROP TABLE pokedex;
DROP TABLE trainer;
DROP TABLE trainer_junction;
-- END DROP SECTION --


-- BEGIN CREATION SECTION --
-- Create New Tables for the start of a new database, comment out if you are not creating/recreating a new database
CREATE TABLE pokedex(
	pokedex_number INTEGER PRIMARY KEY,
	pokemon_name VARCHAR(255) NOT NULL,
	type1 VARCHAR(255) NOT NULL,
	type2 VARCHAR(255),
	ability1 VARCHAR(255) NOT NULL,
	ability2 VARCHAR(255),
	hidden_ability VARCHAR(255),
	base_total INTEGER NOT NULL,
	hp INTEGER NOT NULL,
	attack INTEGER NOT NULL,
	defense INTEGER NOT NULL,
	speed INTEGER NOT NULL,
	sp_attack INTEGER NOT NULL,
	sp_defense INTEGER NOT NULL,
	generation INTEGER NOT NULL,
	is_legendary INTEGER NOT NULL
);

CREATE TABLE trainer(
	trainerID INTEGER PRIMARY KEY,
	trainername VARCHAR(255) NOT null
);

CREATE TABLE trainer_junction(
	tjunction_id INTEGER PRIMARY KEY,
	pokedex_number INTEGER NOT NULL,
	trainerID INTEGER NOT NULL,
	FOREIGN KEY (pokedex_number) REFERENCES pokedex(pokedex_number),
	FOREIGN KEY (trainerID) REFERENCES trainer(trainerID),
	pokelevel INTEGER NOT NULL
);

-- END CREATION SECTION --


-- -- BEGIN UPDATE SECTION --
-- -- If you already have your database created and just want to update, comment this section in to update
-- UPDATE TABLE pokedex;
-- UPDATE TABLE trainer;
-- UDPATE TABLE trainer_junction;
-- -- END UPDATE SECTION --


-- SEARCH FUNCTIONS --
SELECT * FROM trainer LIMIT 20;
SELECT * FROM pokedex LIMIT 20;
SELECT * FROM trainer_junction LIMIT 20;