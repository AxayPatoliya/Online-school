CREATE SEQUENCE s11_sno_seq;
CREATE TABLE s11
(
    sno integer NOT NULL DEFAULT nextval('s11_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    decr text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT s11_pkey PRIMARY KEY (sno)
)
