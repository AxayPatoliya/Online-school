CREATE SEQUENCE clerk_sno_seq;

CREATE TABLE clerk
(
    sno integer NOT NULL DEFAULT nextval('clerk_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    role character varying(550) COLLATE pg_catalog."default" NOT NULL,
    info character varying(550) COLLATE pg_catalog."default" NOT NULL,
    img_file character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT clerk_pkey PRIMARY KEY (sno)
)