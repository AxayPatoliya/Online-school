CREATE SEQUENCE s12_sno_seq;
CREATE TABLE s12
(
    sno integer NOT NULL DEFAULT nextval('s12_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    decr text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT s12_pkey PRIMARY KEY (sno)
)
