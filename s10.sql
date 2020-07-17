CREATE SEQUENCE s10_sno_seq;
CREATE TABLE public.s10
(
    sno integer NOT NULL DEFAULT nextval('s10_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    decr text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT s10_pkey PRIMARY KEY (sno)
)
