CREATE SEQUENCE principal_sno_seq;

CREATE TABLE principal
(
    sno integer NOT NULL DEFAULT nextval('principal_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    info character varying(550) COLLATE pg_catalog."default" NOT NULL,
    img_file character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT principal_pkey PRIMARY KEY (sno)
)