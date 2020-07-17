CREATE SEQUENCE l9_sno_seq;
CREATE TABLE l9
(
    sno integer NOT NULL DEFAULT nextval('l9_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    decr text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT l9_pkey PRIMARY KEY (sno)
)