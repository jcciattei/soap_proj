/* File name: SOAP_schema.sql */
/* Script for the creation of the database tables */
/* Prerequisite: sqlite3 application installed and available on PATH */
/* To run at the command line do: sqlite3 SOAP.db < SOAP_schema.sql */

/* Enable foreign keys */
PRAGMA foreign_keys = ON;

/* For development of schema, drop tables */
DROP TABLE IF EXISTS party_to;
DROP TABLE IF EXISTS manages;
DROP TABLE IF EXISTS rental_agreement;
DROP TABLE IF EXISTS customer_agency;
DROP TABLE IF EXISTS office;

/* Entity tables */
CREATE TABLE customer_agency 
	(agency_id	varchar(5),
	 name		varchar(20) not null,
	 address	varchar(30),
	 city		varchar(20),
	 phone_number	varchar(15),
	 primary key (agency_id)
	);

