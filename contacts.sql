--CREATE SEQUENCE contacts_sno_seq;

CREATE TABLE contacts
(
    sno integer NOT NULL DEFAULT nextval('contacts_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    query text COLLATE pg_catalog."default" NOT NULL,
    date date DEFAULT CURRENT_DATE,
    email character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT contacts_pkey PRIMARY KEY (sno)
)

