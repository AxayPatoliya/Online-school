CREATE SEQUENCE s9_sno_seq;
CREATE TABLE public.s9
(
    sno integer NOT NULL DEFAULT nextval('s9_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    decr text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT s9_pkey PRIMARY KEY (sno)
)
